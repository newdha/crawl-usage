scrapy crawl comment -a product_id=831721 -o 831721_comment.csv
scrapy crawl comment -a product_id=831721 -a sort_type=5 -o 831721_comment_2.csv
scrapy crawl question -a product_id=7564605 -o 7564605_question.csv

python jd/genidf.py -sw ../stop_words.txt ../831721_comment.csv ../comment_idf.txt
python jd/genidf.py -sw ../stop_words.txt ../7564605_question.csv ../question_idf.txt


价|\d+|一|二|三|四|五|六|七|八|九|十|零

启东
南通
海门
崇明
太仓
常熟
昆山
苏州
无锡
嘉兴
平湖
桐乡
海宁
湖州
杭州
绍兴
慈溪

scrapy crawl price -a cities=cities.txt -a start_time=2018-07-14 -a end_time=2018-07-15 -o test.csv