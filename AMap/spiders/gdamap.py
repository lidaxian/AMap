# -*- coding: utf-8 -*-
import scrapy
import re

class GdamapSpider(scrapy.Spider):
    name = 'gdamap'
    allowed_domains = ['amap.com']
    start_urls = ['https://www.amap.com/']

    def parse(self, response):
        url_1 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=3&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=9&city=110000&geoobj=115.65151%7C39.767887%7C116.969869%7C40.440133&keywords=%E9%A3%8E%E6%99%AF%E5%90%8D%E8%83%9C'
        yield scrapy.Request(url=url_1,callback=self.parse_text)

    def parse_text(self,response):
        print(response.text)
        cont =re.findall(r'{"rat.*?cityname":"(.*?)",.*?"shape_region":"(.*?)","longitude".*?address":"(.*?)","cinemazuo_flag.*?id":"(.*?)"name":"(.*?)","group_flag".*?entrances.*?titude":"(.*?)","longitude":"(.*?)".*?"name":"price"},{"type":"text.*?value":"(.*?)","name":"aoi"',response.text)
        print('_))*&^%$#$%^&**************\n\n\r',cont)
