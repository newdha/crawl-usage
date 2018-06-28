import json
from urllib.parse import parse_qs
from urllib.parse import urlparse

import scrapy

from jd.items import QuestionItem


class CommentSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['jd.com']
    question_url = 'http://jd.com/'
    answer_url = 'http://jd.com/'
    
    cur_question_page = 1
    cur_answer_page = 1

    """
    product_id: 产品编号
    same_product：只看当前商品评价
    sort_type：6/时间排序， 5/推荐排序
    """

    def __init__(self, product_id=None, page=1, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        self.cur_question_page = int(page)
        self.question_url = 'http://question.jd.com/question/getQuestionAnswerList.action?productId=%s' % product_id
        self.answer_url = 'http://question.jd.com/question/getAnswerListById.action?'
        
    def _question_url(self, page):
        return self.question_url + '&page=%s' % page
    
    def _answer_url(self, question_id, page):
        return self.answer_url + 'questionId=%s' % question_id + '&page=%s' % page
        
    def start_requests(self):
        yield scrapy.Request(url=self._question_url(self.cur_question_page), callback=self.parse_question)
    
    def parse_answer(self, response):
        self.logger.info('Parse function called on %s', response.url)
        qs = parse_qs(urlparse(response.url).query)
        question_id = qs['questionId'][0]
        cur_page = int(qs['page'][0])
        
        res = json.loads(response.text)
        if len(res['answers']) > 0:
            for answer in res['answers']:
                answer_item = QuestionItem(id=question_id, answer_content=answer['content'], answer_created=answer['created'])
                yield answer_item
                
            yield scrapy.Request(url=self._answer_url(question_id, cur_page + 1), callback=self.parse_answer)
        else:
            self.logger.warn('Stop crawl answer at page %i', cur_page)
        
    def parse_question(self, response):
        self.logger.info('Parse function called on %s', response.url)
        qs = parse_qs(urlparse(response.url).query)
        cur_page = int(qs['page'][0])
        res = json.loads(response.text)
        
        if len(res['questionList']) > 0:
            for question in res['questionList']:
                question_item = QuestionItem(id=question['id'], content=question['content'], created=question['created'])
                yield question_item
                
                if question['answerCount'] > 0:
                    yield scrapy.Request(url=self._answer_url(question['id'], self.cur_answer_page), callback=self.parse_answer)
               
            yield scrapy.Request(url=self._question_url(cur_page + 1), callback=self.parse_question)
        else:
            self.logger.warn('Stop crawl question at page %i', cur_page)
