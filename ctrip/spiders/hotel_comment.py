# -*- coding: utf-8 -*-
import logging 
import re
from time import sleep

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from ctrip.items import CommentItem

logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.INFO)


class HotelCommentSpider(scrapy.Spider):
    name = 'hotel_comment'
    start_url = 'http://hotels.ctrip.com//hotel/{0}.html'
    allowed_domains = ['ctrip.com']
    
    def __init__(self, hotelId=None, *args, **kwargs):
        super(HotelCommentSpider, self).__init__(*args, **kwargs)
        self.start_url = self.start_url.format(hotelId)
        
        chrome_options = Options()
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.implicitly_wait(10)
        
    def closed(self, spider):
        print("spider closed")
#         self.proxy.close()
#         self.server.stop()
        self.browser.close()
    
    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        total_page = int(response.selector.xpath('//input[@id="cTotalPageNum"]/@value').extract_first())
        
        self.browser.get(self.start_url)
        ele = Select(self.browser.find_element_by_class_name('select_sort'))
        ele.select_by_value('1')
        sleep(5)
        
        for page in range(1, total_page + 1):
            print("At page %i" % page)
            if page > 1:
                page_input = self.browser.find_element_by_id('cPageNum')
                page_submit = self.browser.find_element_by_id('cPageBtn')
                page_input.clear()
                page_input.send_keys(page)
                page_submit.click()
                sleep(3)
            
            comments = self.browser.find_elements_by_xpath('//div[@class="comment_detail_list"]/div')
            for comment in comments:
                content = comment.find_element_by_xpath('.//div[@class="J_commentDetail"]').text
                # print(content)
                creation_time = comment.find_element_by_xpath('.//span[@class="time"]').text[3:]
                # print(creation_time)
                useful_vote_count = re.sub("\D", "", comment.find_element_by_xpath('.//div[@class="comment_bar"]//span[@class="n"]').text)
                # print(useful_vote_count)
                score = comment.find_element_by_xpath('.//span[@class="score"]/span').text
                # print(score)
                comment_item = CommentItem(
                    content=content,
                    creation_time=creation_time,
                    useful_vote_count=useful_vote_count,
                    score=score
                )
                yield comment_item
        
