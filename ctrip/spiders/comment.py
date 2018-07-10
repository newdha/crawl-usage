# -*- coding: utf-8 -*-
import re

import scrapy

from ctrip.items import CommentItem


class CommentSpider(scrapy.Spider):
    name = 'comment'
    start_url = 'http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'
    allowed_domains = ['ctrip.com']
    
    def __init__(self, resourceId=None, resourcetype=None, poiID=None, districtId=None, order=1, *args, **kwargs):
        '''
        '''
        super(CommentSpider, self).__init__(*args, **kwargs)
        self.resource_id = resourceId
        self.resource_type = resourcetype
        self.poi_id = poiID
        self.district_id = districtId
        self.order = order
        
    def _query_data(self, page=1):
        return {
            'resourceId':self.resource_id,
            'resourcetype':self.resource_type,
            'poiID' : self.poi_id,
            'districtId': self.district_id,
            'order':str(self.order),
            'pagenow': str(page)
        }
    
    def _request(self, page=1):
        form_data = self._query_data(page)
        return scrapy.FormRequest(
            url=self.start_url,
            method='POST',
            formdata=form_data,
            callback=self.parse
        )
    
    def start_requests(self):
        yield self._request()

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        comments = response.selector.xpath('//div[@itemprop="review"]')
        if len(comments) > 0:
            page = int(response.selector.xpath('//a[@class="current"]/text()').extract_first())
            total_page = int(response.selector.xpath('//b[@class="numpage"]/text()').extract_first())
        
            for comment in comments:
                comment_item = CommentItem(
                    content=comment.xpath('.//li[@itemprop="description"]/span/text()').extract_first(),
                    creation_time=comment.xpath('.//em[@itemprop="datePublished"]/text()').extract_first(),
                    useful_vote_count=comment.xpath('.//span[@class="useful"]/em/text()').extract_first(),
                    score=int(re.sub("\D", "", comment.xpath('.//span[@itemprop="reviewRating"]//span/@style').extract_first())) / 20
                )
                yield comment_item
            
            if page < total_page:
                yield self._request(page=page + 1)
        
