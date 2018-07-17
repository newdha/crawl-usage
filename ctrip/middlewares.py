# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from time import sleep

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver.support.ui import Select


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
class CtripSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CtripDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        
        page = request.meta.get('page', 1)
                    
        spider.browser.get(request.url)
        print(request.url)
        print(spider.browser.title)
        # spider.browser.page_source  # locate page_source
        # print(spider.browser.page_source)
        
#         locator = (By.CLASS_NAME, 'select_sort')
#         WebDriverWait(spider.browser, 50, 1).until(EC.presence_of_element_located(locator))
        
        ele = Select(spider.browser.find_element_by_class_name('select_sort'))
        ele.select_by_value('1')
        sleep(5)
        
            
        if page > 1:
            input = spider.browser.find_element_by_id('cPageNum')
            submit = spider.browser.find_element_by_id('cPageBtn')
            input.clear()
            input.send_keys(page)
            submit.click()
            sleep(5)
        
        sleep(5)
        har = spider.proxy.har
        
        comment_url = ''
        comment_conent = ''

        for entry in har['log']['entries']:
            if 'AjaxHotelCommentList' in entry['request']['url'] and 'orderBy=1' in entry['request']['url']:
                comment_url = entry['request']['url']
                comment_conent = entry['response']['content']['text']
                # print(comment_url)
                # print(comment_conent)
        
        return HtmlResponse(url=comment_url, body=comment_conent, request=request, encoding='utf-8', status=200)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
