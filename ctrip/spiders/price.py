# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.selector import Selector

from ctrip.items import PriceItem


class PriceSpider(scrapy.Spider):
    name = 'price'
    start_url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    allowed_domains = ['ctrip.com']
    
    start_time = ''
    end_time = ''
    city_id = ''
    order_by = '1'
    star = '5'
    
    def __init__(self, city_id=None, start_time=None, end_time=None, order_by='1', star='5', *args, **kwargs):
        '''
        city_id: 城市编号
        start_time：开始时间
        end_time：结束时间
        order_by:排序 1/价格升序
        '''
        super(PriceSpider, self).__init__(*args, **kwargs)
        self.city_id = city_id
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.star = star
        
    def _query_data(self, page=1):
        return {
            'StartTime' : self.start_time,
            'DepTime' : self.end_time,
            'checkIn' : self.start_time,
            'checkOut' : self.end_time,
            'cityId' : self.city_id,
            'star': self.star,
            'orderby': self.order_by,
            'ordertype': '1',
            'page': str(page)
        }
    
    def _request(self, page='1'):
        form_data = self._query_data(page)
        return scrapy.FormRequest(
            url=self.start_url,
            method='POST',
            formdata=form_data,
            callback=self.parse
        )
    
    def start_requests(self):
        yield self._request()

    def _url(self, url):
        return 'http://www.ctrip.com/' + url

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        res = json.loads(response.text)
        main_data = res['HotelMaiDianData']['value']
        page = int(main_data['pageindex'])
        
        total_page = int(Selector(text=res['paging']).xpath('//@data-pagecount').extract()[0])
        
        htllist = json.loads(main_data['htllist'])
        prices = {}
        for htl in htllist:
            prices[htl['hotelid']] = htl['amount']
        
        if len(res['hotelPositionJSON']) > 0:
            for hotel in res['hotelPositionJSON']:
                hotel_item = PriceItem(id=hotel['id'], name=hotel['name'], url=self._url(hotel['url']), score=hotel['score'], dpcount=hotel['dpcount'])
                if hotel['id'] in prices:
                    hotel_item['lowest_price'] = prices[hotel['id']]
                yield hotel_item
            
            if page < total_page:
                yield self._request(page + 1)
        else:
            self.logger.warn('Stop crawl at page %i', page)
