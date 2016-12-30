from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from craigslist_sample.items import CraigslistSampleItem #done last

class MySpider(BaseSpider):
	name = "craig"
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/search/npo"]
	
	def parse(self, response):
		titles = response.selector.xpath("//p")
		items = [] #done last 
		for titles in titles:
			item = CraigslistSampleItem() #done last 
			#title = titles.xpath("a/text()").extract()
			#link = titles.xpath("a/@href").extract()
			item['title'] = titles.xpath("a/text()").extract() #done last 
			item['link']  = titles.xpath("a/@href").extract() #done last 
			items.append(item)#done last 
			#print title, link
		return items 