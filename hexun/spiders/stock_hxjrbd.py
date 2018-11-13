# -*- coding: utf-8 -*-
import json

import scrapy
from w3lib.html import remove_tags

from hexun.items import ArticleItem


class StockHxjrbdSpider(scrapy.Spider):
    name = 'stock_hxjrbd'
    allowed_domains = ['hexun.com']
    
    def __init__(self, *args, **kwargs):
        """
        page:起始页
        """
        super(StockHxjrbdSpider, self).__init__(*args, **kwargs)
        self.list_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=107825103&s=70&priority=0&callback=hx&cp=%s'
        
    def _list_url(self, page):
        return self.list_url + '&cp=%s' % page
    
    def start_requests(self):
        yield scrapy.Request(url=self._list_url(1030), callback=self.parse)
        
    def parse_detail(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        head = response.selector.css('.articleName')
        body = response.selector.css('.art_context')
        
        content = body.xpath('.//div[@class="art_contextBox"]').extract_first()
        if content is None:
            content = body.extract_first()
        
        article_item = ArticleItem(
                    title=head.xpath('.//h1/text()').extract_first(),
                    date_time=head.xpath('.//span[@class="pr20"]/text()').extract_first(),
                    source=head.xpath('.//a[@rel="nofollow"]/text()').extract_first(),
                    content=remove_tags(content)
                )
        yield article_item
    
    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        res = json.loads(response.text.strip()[4:-2])
        
        cur_page = res['currentPage'];
        if len(res['result']) > 0:
            for entity in res['result']:
                yield scrapy.Request(url=entity['entityurl'], callback=self.parse_detail)
                
            yield scrapy.Request(url=self._list_url(cur_page + 1), callback=self.parse)
        else:
            self.logger.warn('Stop crawl answer at page %i', cur_page)
