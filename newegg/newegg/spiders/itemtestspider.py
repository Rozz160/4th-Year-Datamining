from scrapy.spider import Spider
from scrapy.selector import Selector
import re

from newegg.items import NeweggItem

class ItemTestSpider(Spider):
	name = "testitem"
	allowed_domains = ["newegg.com"]
	start_urls = [
		"http://www.newegg.com/Product/Product.aspx?Item=N82E16814121833"
	]
	
	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//html')	
		items = []
		for site in sites:
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
			item['price'] = [re.search("[0-9]+.[0-9]+", priceScript[0]).group()]
			item['numRated'] = site.xpath('//span[contains(@itemprop, "reviewCount")]/text()').extract()
			items.append(item)
		return items