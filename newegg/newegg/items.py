# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NeweggItem(Item):
    # define the fields for your item here like:
	name = Field()
	nameBrand = Field()
	nameGPU = Field()
	coreClock = Field()
	effectiveMem = Field()
	cudaCores = Field()
	memSize = Field()
	rating = Field()
	price = Field()
	numRated = Field()