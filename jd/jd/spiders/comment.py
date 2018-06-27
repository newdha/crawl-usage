import json
from urllib.parse import parse_qs
from urllib.parse import urlparse

import scrapy

from jd.items import CommentItem


class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['jd.com']
    start_url = 'http://jd.com/'
    cur_page = 0

    """
    product_id: 产品编号
    same_product：只看当前商品评价
    sort_type：6/时间排序， 5/推荐排序
    """

    def __init__(self, product_id=None, same_product=True, sort_type=6, page=0, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        self.cur_page = int(page)
        if same_product == bool(True):
            self.start_url = 'http://club.jd.com/comment/skuProductPageComments.action?productId=%s' % product_id
        else:
            self.start_url = 'http://sclub.jd.com/comment/productPageComments.action?productId=%s' % product_id
        self.start_url = self.start_url + '&score=0&sortType=%s&pageSize=10&isShadowSku=0&fold=1' % sort_type
        
    def _request_url(self, page):
        return self.start_url + '&page=%s' % page
        
    def start_requests(self):
        yield scrapy.Request(url=self._request_url(self.cur_page), callback=self.parse)
        
    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        qs = parse_qs(urlparse(response.url).query)
        page = int(qs['page'][0])
        
        res = json.loads(response.text)
        
        if len(res['comments']) > 0:
            for comment in res['comments']:
                comment_item = CommentItem(content=comment['content'], creation_time=comment['creationTime'], score=comment['score'], useful_vote_count=comment['usefulVoteCount'], reply_count=comment['replyCount'])
                if 'afterUserComment' in comment:
                    comment_item['after_user_comment'] = comment['afterUserComment']['hAfterUserComment']['content']
                yield comment_item
            yield scrapy.Request(url=self._request_url(page + 1), callback=self.parse)
        else:
            self.logger.warn('Stop crawl at page %i', page)
