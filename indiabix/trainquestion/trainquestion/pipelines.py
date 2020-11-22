# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
#link for online store
#mongodb+srv://osama:testtest@cluster0.1pmqh.mongodb.net/<dbname>?retryWrites=true&w=majority
class TrainquestionPipeline:

    #collection_name = "silk_deals"

    #def open_spider(self, spider):
        #self.client = pymongo.MongoClient("localhost", 27017)
        #self.db = self.client["IMDB"]

    #def close_spider(self, spider):
        #self.client.close()


    def process_item(self, item, spider):
        #self.db[self.collection_name].insert(item)
        return item
