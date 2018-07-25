# -*- coding: utf-8 -*-
import logging 
import re
from time import sleep

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from ctrip.items import CommentItem


logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.INFO)


class HotelCommentSpider(scrapy.Spider):
    name = 'hotel_comment'
    start_url = 'http://hotels.ctrip.com//hotel/{0}.html'
    allowed_domains = ['ctrip.com']
    
    start_page = 1
    
    def __init__(self, startPage=1, hotelId=None, *args, **kwargs):
        super(HotelCommentSpider, self).__init__(*args, **kwargs)
        self.start_url = self.start_url.format(hotelId)
        
        chrome_options = Options()
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.implicitly_wait(10)
        self.start_page = int(startPage)
        
    def closed(self, spider):
        print("spider closed")
#         self.proxy.close()
#         self.server.stop()
        self.browser.close()
    
    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse, dont_filter=True)
        
    def _gen_comment_item(self, comment):
        content = comment.find_element_by_xpath('.//div[@class="J_commentDetail"]').text
        creation_time = comment.find_element_by_xpath('.//span[@class="time"]').text[3:]
        
        class_name = comment.find_elements_by_tag_name('div')[0].get_attribute('class')
        if 'J_ctrip_pop' in class_name:
            useful_vote_count = re.sub("\D", "", comment.find_element_by_xpath('.//div[@class="comment_bar"]//span[@class="n"]').text)
            score = comment.find_element_by_xpath('.//span[@class="score"]/span').text
        else:
            # 非携程用户
            useful_vote_count = 0
            score = 0
    
        return CommentItem(
                    content=content,
                    creation_time=creation_time,
                    useful_vote_count=useful_vote_count,
                    score=score
                )

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        total_page = int(response.selector.xpath('//input[@id="cTotalPageNum"]/@value').extract_first())
        
        self.browser.get(self.start_url)
        ele = Select(self.browser.find_element_by_class_name('select_sort'))
        ele.select_by_value('1')
        sleep(5)
        
        for page in range(self.start_page, total_page + 1):
            self.logger.info('Process page %s', page)
            if page > 1:
                page_input = self.browser.find_element_by_id('cPageNum')
                page_submit = self.browser.find_element_by_id('cPageBtn')
                page_input.clear()
                page_input.send_keys(page)
                page_submit.click()
                
                try:
                    WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="c_page"]//a[@class="current"]/span'), str(page)))
                except:
                    self.logger.warn('Goto page error at %s', page)
                    next_page = self.browser.find_element_by_class_name('c_down')
                    next_page.click()
                    try:
                        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="c_page"]//a[@class="current"]/span'), str(page)))
                    except:
                        self.logger.warn('Next page error at %s', page)
                        next_page_index = self.browser.find_element_by_xpath('//div[@class="c_page"]//a[@value="' + str(page) + '"]')
                        next_page_index.click()
                        
                        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="c_page"]//a[@class="current"]/span'), str(page)))
                sleep(1)
            
            comments = self.browser.find_elements_by_xpath('//div[@class="comment_detail_list"]/div')
            for comment in comments:
                comment_item = self._gen_comment_item(comment)
                
                yield comment_item
        
