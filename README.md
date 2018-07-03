scrapy crawl comment -a product_id=831721 -o 831721_comment.csv
scrapy crawl comment -a product_id=831721 -a sort_type=5 -o 831721_comment_2.csv
scrapy crawl question -a product_id=7564605 -o 7564605_question.csv

python jd/genidf.py -sw ../stop_words.txt ../831721_comment.csv ../comment_idf.txt
python jd/genidf.py -sw ../stop_words.txt ../7564605_question.csv ../question_idf.txt


价|\d+|一|二|三|四|五|六|七|八|九|十|零

scrapy crawl price -a cities=cities.txt -a start_time=2018-07-09 -a end_time=2018-07-10 -o 2018-07-09.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-10 -a end_time=2018-07-11 -o 2018-07-10.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-11 -a end_time=2018-07-12 -o 2018-07-11.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-12 -a end_time=2018-07-13 -o 2018-07-12.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-13 -a end_time=2018-07-14 -o 2018-07-13.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-14 -a end_time=2018-07-15 -o 2018-07-14.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-15 -a end_time=2018-07-16 -o 2018-07-15.csv
scrapy crawl price -a cities=cities.txt -a start_time=2018-07-16 -a end_time=2018-07-17 -o 2018-07-16.csv

scrapy crawl price -a cities=cities.txt -a start_time=2018-07-06 -a end_time=2018-08-03 -o test.csv
