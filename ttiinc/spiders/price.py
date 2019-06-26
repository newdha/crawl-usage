# -*- coding: utf-8 -*-
import json

import scrapy

from ttiinc.items import DiodeItem


class PriceSpider(scrapy.Spider):
    name = 'price'
    start_url = 'https://www.ttiinc.com/bin/services/processData?jsonPayloadAvailable=true&osgiService=partsearchpost'
    allowed_domains = ['ttiinc.com']
    
    def __init__(self, *args, **kwargs):
        '''
        '''
        super(PriceSpider, self).__init__(*args, **kwargs)
        
    def _query_data(self, page=1):
        return {"searchTerms":"rf diode",
                "inStock":"",
                "rohsCompliant":"",
                "leadFree":"",
                "containsLead":"",
                "pageNum": str(page)
                }
    
    def _request(self, page=1):
        data = self._query_data(page)
        return scrapy.Request(
            url=self.start_url,
            # meta={"proxy":"http://127.0.0.1:9090"},
            method='POST',
            headers={"Content-Type":"application/json;charset=UTF-8"},
            cookies={"visid_incap_731139": "1ktFbNjYRWuBoygTPtdiFZc7E10AAAAAQUIPAAAAAABFXRQHcQAP8TX0tpDGC++v", "incap_ses_637_731139":"f/M1WdvTs3dB7d4TNRXXCJc7E10AAAAAXuT4/9f4WuEgXKAemvX4+w==", "renderid":"rend01", "AMCV_474027E253DB53E90A490D4E%40AdobeOrg:":"-1303530583%7CMCIDTS%7C18074%7CvVersion%7C3.3.0", "check":"true", "mbox":"session#3a171e32bffc46738800b01661a552bb#1561543438"},
            body=json.dumps(data),
            callback=self.parse
        )
    
    def start_requests(self):
        yield self._request()

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        res = json.loads(response.text)
        page = res["pageNum"]
        total_page = res["numPages"]
        records = res["parts"]["records"]
        if len(records) > 0:
            for record in records:
                diode_item = DiodeItem(
                    mfn=record['mfrPartNumber'],
                    stock=record['availableToSell'] if 'availableToSell' in record else '' ,
                    price=record['prices'][0]['price'],
                    desc=record['partsDescription']
                )
                yield diode_item
                
            if page < total_page:
                yield self._request(page=page + 1)
        else:
            self.logger.warn('Stop crawl at page %i', page)
        yield
        
