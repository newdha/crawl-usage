# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    city_name = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    dpcount = scrapy.Field()
    date = scrapy.Field()
    lowest_price = scrapy.Field()
