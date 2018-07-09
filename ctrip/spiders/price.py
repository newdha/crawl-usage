# -*- coding: utf-8 -*-
import datetime
import json

import scrapy
from scrapy.selector import Selector

from ctrip.items import PriceItem
import utils


class PriceSpider(scrapy.Spider):
    name = 'price'
    start_url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    allowed_domains = ['ctrip.com']
    
    def __init__(self, cities=None, start_time=None, end_time=None, order_by='1', star='5', equip='', *args, **kwargs):
        '''
        city_id: 城市列表文件
        start_time：开始时间
        end_time：结束时间
        order_by:排序 1/价格升序
        '''
        super(PriceSpider, self).__init__(*args, **kwargs)
        self.cities = cities
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.star = star
        self.equip = equip
        
    def _query_data(self, city_id=None, start_time=None, end_time=None, page=1):
        return {
            'StartTime' : datetime.datetime.strftime(start_time, '%Y-%m-%d'),
            'DepTime' : datetime.datetime.strftime(end_time, '%Y-%m-%d'),
            'checkIn' : datetime.datetime.strftime(start_time, '%Y-%m-%d'),
            'checkOut' : datetime.datetime.strftime(end_time, '%Y-%m-%d'),
            'cityId' : str(city_id),
            'star': self.star,
            'equip': self.equip,
            'orderby': self.order_by,
            'ordertype': '1',
            'page': str(page),
        }
    
    def _request(self, city_id=None, start_time=None, end_time=None, page='1'):
        form_data = self._query_data(city_id, start_time, end_time, page)
        return scrapy.FormRequest(
            url=self.start_url,
            method='POST',
            formdata=form_data,
            callback=self.parse
        )
    
    def start_requests(self):
        cities = utils.read_pairs(self.cities).keys()
        
        if ',' in self.start_time:
            for d in self.start_time.split(','):
                start_time = datetime.datetime.strptime(d, '%Y-%m-%d')
                end_time = start_time + datetime.timedelta(days=1)
                for city_id in cities:
                    yield self._request(city_id=city_id, start_time=start_time, end_time=end_time) 
        else:
            self.start_time = datetime.datetime.strptime(self.start_time, '%Y-%m-%d')
            if self.end_time:
                self.end_time = datetime.datetime.strptime(self.end_time, '%Y-%m-%d')
            else:
                self.end_time = self.start_time + datetime.timedelta(days=1)
            
            delta = (self.end_time - self.start_time).days;
            for offset in range(delta):
                start_time = self.start_time + datetime.timedelta(days=offset)
                end_time = start_time + datetime.timedelta(days=1)
                for city_id in cities:
                    yield self._request(city_id=city_id, start_time=start_time, end_time=end_time)

    def _url(self, url):
        return 'http://hotels.ctrip.com/' + url

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        res = json.loads(response.text)
        main_data = res['HotelMaiDianData']['value']
        page = int(main_data['pageindex'])
        cityname = main_data['cityname']
        cityid = main_data['cityid']
        starttime = datetime.datetime.strptime(main_data['starttime'], '%Y-%m-%d')
        endtime = datetime.datetime.strptime(main_data['endtime'], '%Y-%m-%d') 
        
        total_page = int(Selector(text=res['paging']).xpath('//@data-pagecount').extract()[0])
        
        htllist = json.loads(main_data['htllist'])
        prices = {}
        for htl in htllist:
            prices[htl['hotelid']] = htl['amount']
        
        if len(res['hotelPositionJSON']) > 0:
            for hotel in res['hotelPositionJSON']:
                hotel_item = PriceItem(
                    id=hotel['id'],
                    name=hotel['name'],
                    city_name=cityname,
                    url=self._url(hotel['url']),
                    score=hotel['score'],
                    dpcount=hotel['dpcount'],
                    date=main_data['starttime']
                )
                if hotel['id'] in prices:
                    hotel_item['lowest_price'] = prices[hotel['id']]
                yield hotel_item
            
            if page < total_page:
                yield self._request(city_id=cityid, start_time=starttime, end_time=endtime, page=page + 1)
        else:
            self.logger.warn('Stop crawl at page %i', page)
