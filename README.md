scrapy crawl comment -a product_id=5174007 -o 5174007_comment.csv
scrapy crawl comment -a product_id=831721 -a sort_type=5 -o 831721_comment_2.csv
scrapy crawl question -a product_id=5174007 -o 5174007_question.csv

python jd/genidf.py -sw ../stop_words.txt ../831721_comment.csv ../comment_idf.txt
python jd/genidf.py -sw ../stop_words.txt ../7564605_question.csv ../question_idf.txt


价|\d+|一|二|三|四|五|六|七|八|九|十|零

scrapy crawl price -a cities=cities.txt -a start_time=2018-07-09 -a end_time=2018-07-10 -o 2018-07-09.csv

scrapy crawl price -a cities=cities.txt -a equip=3 -a start_time=2018-07-10,2018-07-07,2018-07-14,2018-07-21,2018-07-28 -o swim.csv

scrapy crawl price -a cities=cities.txt -a equip=3 -a start_time=2018-08-14,2018-08-04,2018-08-11,2018-08-18,2018-08-25 -o xian.csv

scrapy crawl scene_comment -a resourceId=1444 -a resourcetype=2 -a poiID=75682 -a districtId=7 -o 秦始皇兵马俑博物馆.csv
scrapy crawl scene_comment -a resourceId=5420 -a resourcetype=2 -a poiID=76739 -a districtId=7 -o 秦始皇陵.csv
4小时
坐游5（306），不坐914
直接携程订门票，刷身份证进去，免去排队的烦恼，自己请讲解
近华清池
兵马俑大门口的肯德基旁边坐免费大巴穿梭车去秦始皇陵
scrapy crawl scene_comment -a resourceId=1446 -a resourcetype=2 -a poiID=75684 -a districtId=7 -o 陕西历史博物馆.csv
4-5小时
每天的特定时段有集体的免费讲解服务
每周一闭馆
网上预约
scrapy crawl scene_comment -a resourceId=1449 -a resourcetype=2 -a poiID=75686 -a districtId=7 -o 西安城墙.csv
3-4小时
scrapy crawl scene_comment -a resourceId=26184 -a resourcetype=2 -a poiID=81938 -a districtId=7 -o 大唐芙蓉园.csv
白天3+晚上2
scrapy crawl scene_comment -a resourceId=136558 -a resourcetype=2 -a poiID=10758966 -a districtId=7 -o 长恨歌演出.csv
1小时（晚上）
scrapy crawl scene_comment -a resourceId=54080 -a resourcetype=2 -a poiID=10559031 -a districtId=7 -o 回民街.csv
3-5小时
scrapy crawl scene_comment -a resourceId=1410344 -a resourcetype=2 -a poiID=13219372 -a districtId=7 -o 西安鼓楼.csv
1小时
scrapy crawl scene_comment -a resourceId=52702 -a resourcetype=2 -a poiID=84631 -a districtId=7 -o 西安钟楼.csv
1小时
scrapy crawl scene_comment -a resourceId=73279 -a resourcetype=2 -a poiID=89229 -a districtId=7 -o 秦岭野生动物园.csv
4-5小时
scrapy crawl scene_comment -a resourceId=1443 -a resourcetype=2 -a poiID=75681 -a districtId=7 -o 华清宫.csv
scrapy crawl scene_comment -a resourceId=6087 -a resourcetype=2 -a poiID=76835 -a districtId=7 -o 骊山.csv
2-4小时
scrapy crawl scene_comment -a resourceId=1442 -a resourcetype=2 -a poiID=75680 -a districtId=7 -o 大雁塔大慈恩寺.csv
1-2小时
scrapy crawl scene_comment -a resourceId=52697 -a resourcetype=2 -a poiID=84628 -a districtId=7 -o 曲江海洋极地公园.csv
scrapy crawl scene_comment -a resourceId=1702601 -a resourcetype=2 -a poiID=21012895 -a districtId=7 -o 曲江海洋公园3D错觉体验馆.csv
4-5小时
scrapy crawl scene_comment -a resourceId=140439 -a resourcetype=2 -a poiID=101097 -a districtId=7 -o 西安碑林博物馆.csv
3-5小时
scrapy crawl scene_comment -a resourceId=52685 -a resourcetype=2 -a poiID=84625 -a districtId=7 -o 大明宫国家遗址公园.csv
3-4小时
scrapy crawl scene_comment -a resourceId=54079 -a resourcetype=2 -a poiID=84692 -a districtId=7 -o 大雁塔北广场.csv
0.5小时（晚上）
scrapy crawl scene_comment -a resourceId=1440 -a resourcetype=2 -a poiID=75678 -a districtId=7 -o 翠华山.csv
3-4小时
scrapy crawl scene_comment -a resourceId=5418 -a resourcetype=2 -a poiID=76737 -a districtId=7 -o 小雁塔荐福寺.csv
1-2小时
scrapy crawl scene_comment -a resourceId=52727 -a resourcetype=2 -a poiID=84640 -a districtId=7 -o 书院门文化街.csv
1-2小时
scrapy crawl scene_comment -a resourceId=52677 -a resourcetype=2 -a poiID=10532757 -a districtId=7 -o 西安博物院.csv
2小时
scrapy crawl scene_comment -a resourceId=73059 -a resourcetype=2 -a poiID=89194 -a districtId=7 -o 高家大院.csv
2小时
scrapy crawl scene_comment -a resourceId=1441 -a resourcetype=2 -a poiID=75679 -a districtId=7 -o 半坡博物馆.csv
1-2小时
scrapy crawl scene_comment -a resourceId=61255 -a resourcetype=2 -a poiID=86684 -a districtId=7 -o 曲江池遗址公园.csv
1-3小时
scrapy crawl scene_comment -a resourceId=1445 -a resourcetype=2 -a poiID=75683 -a districtId=7 -o 化觉巷清真大寺.csv
2小时
scrapy crawl scene_comment -a resourceId=73315 -a resourcetype=2 -a poiID=89241 -a districtId=7 -o 关中民俗艺术博物院.csv
1-2小时
scrapy crawl scene_comment -a resourceId=140429 -a resourcetype=2 -a poiID=101091 -a districtId=7 -o 大唐西市博物馆.csv
2-3小时
scrapy crawl scene_comment -a resourceId=72252 -a resourcetype=2 -a poiID=88969 -a districtId=7 -o 太平国家森林公园.csv
4-5小时
scrapy crawl scene_comment -a resourceId=5421 -a resourcetype=2 -a poiID=76740 -a districtId=7 -o 西安事变纪念馆.csv
1-2小时
scrapy crawl scene_comment -a resourceId=52708 -a resourcetype=2 -a poiID=84633 -a districtId=7 -o 曲江寒窑遗址公园.csv
1-2小时
scrapy crawl scene_comment -a resourceId=52679 -a resourcetype=2 -a poiID=84623 -a districtId=7 -o 广仁寺.csv
1-2小时