# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request   

class BookPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta = {'bookname': item.get('book_name')}) for u in urls]
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = request.meta['bookname'].replace(':','')
        return f'full/{image_guid}.jpg'
    
