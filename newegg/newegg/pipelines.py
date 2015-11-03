# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import MySQLdb

class NeweggPipeline(object):
	def __init__(self): 
		conn = MySQLdb.connect(host="localhost",user="root",passwd="0000",db="scrapydb")
		cursor = conn.cursor()
		cursor.execute("DROP TABLE IF EXISTS items")
		sqlStmnt=("CREATE TABLE items("
			"Id INT PRIMARY KEY AUTO_INCREMENT, "
			"Rating INT NULL, "
			"NumberRated INT NULL, "
			"Price FLOAT NULL, "
			"Name VARCHAR(45) NOT NULL, "
			"NameBrand VARCHAR(45) NOT NULL, "
			"NameGPU VARCHAR(45) NOT NULL, "
			"CoreClock VARCHAR(25) NULL, "
			"CudaCores VARCHAR(25) NULL, "
			"EffectiveMemory VARCHAR(45) NULL, "
			"MemorySize VARCHAR(25) NULL"
			")")
		cursor.execute(sqlStmnt)
		conn.close()
		
	def process_item_value(self, name):
		if name == "price":	
			try:
				return float(self.item[name][0])
			except:
				return 0.0
		elif (name == "rating") or (name == "numRated"):
			try:
				return int(self.item[name][0])
			except:
				return 0
		else:
			try:
				return self.item[name][0]
			except:
				return None
				
	def process_sql(self):
		conn = MySQLdb.connect(host="localhost",user="root",passwd="0000",db="scrapydb")
		cursor = conn.cursor()
	
		try:
			cursor.execute("INSERT INTO items("
				"Rating, NumberRated, Price, Name, NameBrand, NameGPU, CoreClock, CudaCores, EffectiveMemory, MemorySize"
				") VALUES (%d, %d, %f, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" 
				% (self.rating, self.numRated, self.price, self.item["name"][0], self.item["nameBrand"][0], self.item["nameGPU"][0], self.coreClock, self.cudaCores, self.effectiveMem, self.memSize))
			conn.commit()
			print("INSERTED INTO TABLE")
		except MySQLdb.Error, e: 
			print("Error inserting")
			conn.rollback()
			try:
				print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
			except IndexError:
				print "MySQL Error: %s" % str(e)
			
		conn.close()
		
	def process_item(self, item, spider):
		if not (item["name"] and item["nameBrand"] and item["nameGPU"]):
			raise DropItem("Missing key elements in %s" % item)
		elif not ((item["name"][0] == "AMD") or (item["name"][0] == "ATI") or (item["name"][0] == "NVIDIA")):
			raise DropItem("Incorrect format within %s" % item)
		
		self.item = item
		self.memSize = self.process_item_value("memSize")
		self.effectiveMem = self.process_item_value("effectiveMem")
		self.coreClock = self.process_item_value("coreClock")
		self.cudaCores = self.process_item_value("cudaCores")
		self.rating = self.process_item_value("rating")
		self.numRated = self.process_item_value("numRated")
		self.price = self.process_item_value("price")
		
		self.process_sql()
		
		return item
