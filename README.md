scrapy crawl stock_hxjrbd -o stock_hxjrbd.json

scrapy crawl comment -a product_id=5267712 -o 5267712_comment.csv
scrapy crawl comment -a product_id=1318300 -o 1318300_comment.csv
scrapy crawl comment -a product_id=4899954 -o 4899954_comment.csv
scrapy crawl comment -a product_id=4979498 -o 4979498_comment.csv


scrapy crawl comment -a product_id=2865858 -o 2865858_comment.csv
scrapy crawl question -a product_id=2865858 -o 2865858_question.csv

python jd/genidf.py -sw ../stop_words.txt ../831721_comment.csv ../comment_idf.txt
python jd/genidf.py -sw ../stop_words.txt ../7564605_question.csv ../question_idf.txt


价|\d+|一|二|三|四|五|六|七|八|九|十|零

scrapy crawl price -a cities=cities.txt -a start_time=2018-07-09 -a end_time=2018-07-10 -o 2018-07-09.csv

scrapy crawl price -a cities=cities.txt -a equip=3 -a start_time=2018-09-19,2018-10-03,2018-10-10 -o swim.csv

scrapy crawl price -a cities=cities.txt -a equip=3 -a star=5,4 -a start_time=2018-10-03,2018-10-10,2018-10-24 -o haining.csv

scrapy crawl hotel_comment -a hotelId=1303455 -o 1303455.csv
scrapy crawl hotel_comment -a hotelId=420015 -a startPage=225 -o 420015.csv

scrapy crawl scene_comment -a resourceId=61319 -a resourcetype=4 -a poiID=102171 -a districtId=86 -o 海宁中国皮革城.csv
scrapy crawl scene_comment -a resourceId=5420 -a resourcetype=2 -a poiID=76739 -a districtId=7 -o 秦始皇陵.csv
scrapy crawl scene_comment -a resourceId=136558 -a resourcetype=2 -a poiID=10758966 -a districtId=7 -o 长恨歌演出.csv
scrapy crawl scene_comment -a resourceId=1443 -a resourcetype=2 -a poiID=75681 -a districtId=7 -o 华清宫.csv
scrapy crawl scene_comment -a resourceId=6087 -a resourcetype=2 -a poiID=76835 -a districtId=7 -o 骊山.csv
scrapy crawl scene_comment -a resourceId=5421 -a resourcetype=2 -a poiID=76740 -a districtId=7 -o 西安事变纪念馆.csv
4小时
长恨歌演出1小时（晚上）
坐游5（306），不坐914
直接携程订门票，刷身份证进去，免去排队的烦恼，自己请讲解
近华清池
兵马俑大门口的肯德基旁边坐免费大巴穿梭车去秦始皇陵
scrapy crawl scene_comment -a resourceId=1449 -a resourcetype=2 -a poiID=75686 -a districtId=7 -o 西安城墙.csv
scrapy crawl scene_comment -a resourceId=140439 -a resourcetype=2 -a poiID=101097 -a districtId=7 -o 西安碑林博物馆.csv
scrapy crawl scene_comment -a resourceId=52685 -a resourcetype=2 -a poiID=84625 -a districtId=7 -o 大明宫国家遗址公园.csv
scrapy crawl scene_comment -a resourceId=52727 -a resourcetype=2 -a poiID=84640 -a districtId=7 -o 书院门文化街.csv
碑林博物馆 8:00-18:15
博物馆在永宁门附近
尚武门，就是唐朝玄武门事变的旧址
一般到西安旅游的人都会选择走南门（永宁门）入口。永宁门是保存最完好，规模最大的一道城门，接待习主席和外国友人时，演出便安排在这道城门
建议下午过了最热的时候去。提倡的攻略应该是从南门离落日两个小时左右的时候登上城墙
scrapy crawl scene_comment -a resourceId=1446 -a resourcetype=2 -a poiID=75684 -a districtId=7 -o 陕西历史博物馆.csv
scrapy crawl scene_comment -a resourceId=26184 -a resourcetype=2 -a poiID=81938 -a districtId=7 -o 大唐芙蓉园.csv
scrapy crawl scene_comment -a resourceId=1442 -a resourcetype=2 -a poiID=75680 -a districtId=7 -o 大雁塔大慈恩寺.csv
scrapy crawl scene_comment -a resourceId=52697 -a resourcetype=2 -a poiID=84628 -a districtId=7 -o 曲江海洋极地公园.csv
scrapy crawl scene_comment -a resourceId=1702601 -a resourcetype=2 -a poiID=21012895 -a districtId=7 -o 曲江海洋公园3D错觉体验馆.csv
scrapy crawl scene_comment -a resourceId=54079 -a resourcetype=2 -a poiID=84692 -a districtId=7 -o 大雁塔北广场.csv
scrapy crawl scene_comment -a resourceId=61255 -a resourcetype=2 -a poiID=86684 -a districtId=7 -o 曲江池遗址公园.csv
scrapy crawl scene_comment -a resourceId=52708 -a resourcetype=2 -a poiID=84633 -a districtId=7 -o 曲江寒窑遗址公园.csv
博物馆建议网上预约，每周一闭馆，每天的特定时段有集体的免费讲解服务
芙蓉园观光车是完全用不到
芙蓉园演出时间表
唐僧，法相宗
大雁塔南北广场、以及周围的唐城墙遗址公园、曲江池遗址公园、曲江南湖都是风景秀丽古色古香得美景，而且都免费
周边还有曲江海洋世界是中国第三大海洋馆。大唐芙蓉园
大雁塔最好晚上去，20左右到可以看到音乐喷泉，最好别周二去，场地检修
白天3+晚上2
scrapy crawl scene_comment -a resourceId=54080 -a resourcetype=2 -a poiID=10559031 -a districtId=7 -o 回民街.csv
scrapy crawl scene_comment -a resourceId=1410344 -a resourcetype=2 -a poiID=13219372 -a districtId=7 -o 西安鼓楼.csv
scrapy crawl scene_comment -a resourceId=52702 -a resourcetype=2 -a poiID=84631 -a districtId=7 -o 西安钟楼.csv
scrapy crawl scene_comment -a resourceId=73059 -a resourcetype=2 -a poiID=89194 -a districtId=7 -o 高家大院.csv
scrapy crawl scene_comment -a resourceId=1445 -a resourcetype=2 -a poiID=75683 -a districtId=7 -o 化觉巷清真大寺.csv
3-5小时
钟鼓楼表演，每半小时有一场表演
上午9时、正午12时、下午3时还可以观看“晨钟暮鼓”的仿古表演
鼓楼每日表演六场，时间分别为：上午：9:00 10:00 11:00 下午：14:30 16:30 17:30
高家大院表演
scrapy crawl scene_comment -a resourceId=73279 -a resourcetype=2 -a poiID=89229 -a districtId=7 -o 秦岭野生动物园.csv
4-5小时
scrapy crawl scene_comment -a resourceId=1440 -a resourcetype=2 -a poiID=75678 -a districtId=7 -o 翠华山.csv
3-4小时
scrapy crawl scene_comment -a resourceId=5418 -a resourcetype=2 -a poiID=76737 -a districtId=7 -o 小雁塔荐福寺.csv
scrapy crawl scene_comment -a resourceId=52677 -a resourcetype=2 -a poiID=10532757 -a districtId=7 -o 西安博物院.csv
2小时
scrapy crawl scene_comment -a resourceId=1441 -a resourcetype=2 -a poiID=75679 -a districtId=7 -o 半坡博物馆.csv
1-2小时
scrapy crawl scene_comment -a resourceId=73315 -a resourcetype=2 -a poiID=89241 -a districtId=7 -o 关中民俗艺术博物院.csv
1-2小时
scrapy crawl scene_comment -a resourceId=140429 -a resourcetype=2 -a poiID=101091 -a districtId=7 -o 大唐西市博物馆.csv
2-3小时
scrapy crawl scene_comment -a resourceId=72252 -a resourcetype=2 -a poiID=88969 -a districtId=7 -o 太平国家森林公园.csv
4-5小时
scrapy crawl scene_comment -a resourceId=52679 -a resourcetype=2 -a poiID=84623 -a districtId=7 -o 广仁寺.csv
1-2小时