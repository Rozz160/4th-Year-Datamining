from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re
import MySQLdb

from newegg.items import NeweggItem

class NewEggSpider(CrawlSpider):
	name = "newegg"
	allowed_domains = ["newegg.com"]
	start_urls = [
		"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/"
	]
	
	def page_js_process(value):
		m = re.search("Page-[0-9]+", value)
		if m:
			return m.group()
	
	rules = (
		Rule(SgmlLinkExtractor(allow=(r'.+', ), restrict_xpaths=('//a[@class="next"]',), process_value=page_js_process
		), follow=True),
		Rule(SgmlLinkExtractor(allow=(r'.+'), restrict_xpaths=('//div[@class="wrapper"]/a',)
		), callback="parse_item", follow=True),
	)
	
	def parse_item(self, response):
		sel = Selector(response)
		site = sel.xpath('//html')	
		item = NeweggItem()
		
		specs = site.xpath('//div[contains(@id, "Specs")]')
		item['nameBrand'] = specs.xpath('fieldset[1]/dl[1]/dd/text()').extract()
		item['name'] = specs.xpath('fieldset[3]/dl[1]/dd/text()').extract()
		item['nameGPU'] = specs.xpath('fieldset[3]/dl[2]/dd/text()').extract()
		if "Core Clock" in specs.xpath('fieldset[3]/dl[3]/dt/text()').extract():
			item['coreClock'] = specs.xpath('fieldset[3]/dl[3]/dd/text()').extract()
		if "CUDA Cores" or "Stream" in specs.xpath('fieldset[3]/dl[5]/dt/text()').extract():
			item['cudaCores'] = specs.xpath('fieldset[3]/dl[5]/dd/text()').extract()
		if "Effective Memory Clock" in specs.xpath('fieldset[4]/dl[1]/dt/text()').extract():
			item['effectiveMem'] = specs.xpath('fieldset[4]/dl[1]/dd/text()').extract()
			item['memSize'] = specs.xpath('fieldset[4]/dl[2]/dd/text()').extract()
		else:
			item['memSize'] = specs.xpath('fieldset[4]/dl[1]/dd/text()').extract()
		item['rating'] = site.xpath('//a[contains(@class, "itmRating")]/span[1]/@content').extract()
		priceScript = site.xpath('//script[contains(text(), "product_sale_price")]/text()').re('product_sale_price:\[\'[0-9]+.[0-9]+\'\]')
		if priceScript:
			item['price'] = [re.search("[0-9]+.[0-9]+", priceScript[0]).group()]
		item['numRated'] = site.xpath('//span[contains(@itemprop, "reviewCount")]/text()').extract()
		
		return item
		
	
