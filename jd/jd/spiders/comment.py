import json

import scrapy

from jd.items import CommentItem


class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    """
    product_id: 产品编号
    same_product：只看当前商品评价
    sort_type：6/时间排序， 5/推荐排序
    """

    def __init__(self, product_id=None, same_product=True, sort_type=6, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        if same_product:
            self.start_urls = 'http://club.jd.com/comment/skuProductPageComments.action?productId=%s' % product_id
        else:
            self.start_urls = 'http://sclub.jd.com/comment/productPageComments.action?productId=%s' % product_id
        self.start_urls = [self.start_urls + '&score=0&sortType=%s&page=0&pageSize=10&isShadowSku=0&fold=1' % sort_type]
        
    def parse(self, response):
        res = json.loads(response.text)
        
        for comment in res['comments']:
            print("comment: " + comment['content'])
            
            comment_item = CommentItem(content=comment['content'], creation_time=comment['creationTime'], score=comment['score'], useful_vote_count=comment['usefulVoteCount'], reply_count=comment['replyCount'])
            if 'afterUserComment' in comment:
                comment_item['after_user_comment'] = comment['afterUserComment']['hAfterUserComment']['content']
            yield comment_item
