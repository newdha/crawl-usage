# -*- coding: utf-8 -*-
import json
import logging 
import re

from browsermobproxy import Server
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ctrip.items import CommentItem

logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.INFO)


class HotelCommentSpider(scrapy.Spider):
    name = 'hotel_comment'
    start_url = 'http://hotels.ctrip.com//hotel/{0}.html'
    allowed_domains = ['ctrip.com']
    
    def __init__(self, maxPage=None, hotelId=None, *args, **kwargs):
        super(HotelCommentSpider, self).__init__(*args, **kwargs)
        self.max_page = int(maxPage)
        self.start_url = self.start_url.format(hotelId)
        
        self.server = Server(r'/Users/dha/tools/browsermob-proxy-2.1.4/bin/browsermob-proxy')
        self.server.start()
        self.proxy = self.server.create_proxy()
        
        chrome_options = Options()
        #chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.implicitly_wait(10)
        
    def closed(self, spider):
        print("spider closed")
        self.proxy.close()
        self.server.stop()
        #self.browser.close()
    
    def start_requests(self):
        self.proxy.blacklist('.*accounts.google.com.*', 400)
        self.proxy.new_har(self.start_url, options={'captureHeaders': True, 'captureContent':True})
        for page in range(1, self.max_page + 1):
            yield scrapy.Request(url=self.start_url, callback=self.parse, meta={'page':page}, dont_filter=True)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        comments = response.selector.xpath('//div[@class="comment_detail_list"]/div')
        for comment in comments:
            comment_item = CommentItem(
                content=comment.xpath('.//div[@class="J_commentDetail"]/text()').extract_first(),
                creation_time=comment.xpath('.//span[@class="time"]/text()').extract_first(),
                useful_vote_count=comment.xpath('.//a[@class="useful"]/span/text()').extract_first(),
                score=comment.xpath('.//span[@class="score"]/span/text()').extract_first()
            )
            yield comment_item
        
