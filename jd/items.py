# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    content = scrapy.Field()
    creation_time = scrapy.Field()
    useful_vote_count = scrapy.Field()
    score = scrapy.Field()
    reply_count = scrapy.Field()
    after_user_comment = scrapy.Field()
    pass


class QuestionItem(scrapy.Item):
    id = scrapy.Field()
    content = scrapy.Field()
    created = scrapy.Field()
    answer_created = scrapy.Field()
    answer_content = scrapy.Field()
