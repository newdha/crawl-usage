scrapy crawl comment -a product_id=831721 -o 831721_comment.csv
scrapy crawl comment -a product_id=831721 -a sort_type=5 -o 831721_comment_2.csv
scrapy crawl question -a product_id=7564605 -o 7564605_question.csv

python jd/genidf.py -sw ../stop_words.txt ../831721_comment.csv ../comment_idf.txt
python jd/genidf.py -sw ../stop_words.txt ../7564605_question.csv ../question_idf.txt


价|\d+|一|二|三|四|五|六|七|八|九|十|零