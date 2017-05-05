# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule, Request ##CrawlSpider与Rule配合使用可以骑到历遍全站的作用、Request干啥的我就不解释了
from scrapy.linkextractors import LinkExtractor ##配合Rule进行URL规则匹配
from qunaer.items import QunaerItem ##不解释
# from scrapy import FormRequest ##Scrapy中用作登录使用的一个包

class QunaerurlSpider(CrawlSpider):
    name = "qunaerurl"
    allowed_domains = ["ctrip.com"]
    start_urls = ['http://www.ctrip.com/']

    rules = (
    	Rule(LinkExtractor(allow=('\.html',)),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
    	title_in_a_page = response.xpath('/html/head/title/text()')
    	# print title_in_a_page.extract()

    	item = QunaerItem()

    	try:
    		item['link_title'] = title_in_a_page.extract()[0]
    		item['link_a'] = response.url
    	except:
    		pass
    	return item

