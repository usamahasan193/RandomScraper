import scrapy
from scrapy_selenium import SeleniumRequest

class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://www.aliexpress.com/category/100003070/men-clothing.html',
            wait_time= 100,
            callback= self.parse
        )

    def parse(self, response):
       # items = response.xpath("//a[@class = 'item-title']")
        #for item in items:
       title = response.xpath("//a[@class = 'item-title']/text()").getall()
       yield {
           'tille': title
       }
            #links = item.xpath(".//@href").get()

