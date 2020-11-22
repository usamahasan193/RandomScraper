import scrapy
from scrapy_selenium import SeleniumRequest

class SlikdealsSpider(scrapy.Spider):
    name = 'slikdeals'

    def start_requests(self):
         yield SeleniumRequest(
             url = "https://slickdeals.net/newsearch.php?src=SearchBar&q=laptop&searcharea=deals&searchin=first",
             wait_time= 5,
             callback= self.parse
         )

    def parse(self, response):
        products = response.xpath("//div[@class = 'resultRow']")
        for product in products:
            title =  product.xpath(".//div[@class = 'dealWrapper']/a/@title").get()
            link =  product.xpath(".//div[@class = 'dealWrapper']/a/@href").get()

            yield {
                'title': title,
                'link': link
            }
