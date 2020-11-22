import scrapy
from scrapy_selenium import SeleniumRequest

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=1&q=iphone&spm=a2o2r4.tm80022604.search.go.45b4986bKKlnjZ',
            wait_time=5,
            callback=self.parse
        )
    
    def parse(self, response):
        items = response.xpath("//div[@class = 'c16H9d']")
        for item in items:
            title = item.xpath(".//a/text()").get()
            links = item.xpath(".//a/@href").get()
            
            yield {
                'title': title,
                'link': links
            }
        for i in range(2, 20):
            absolute_url = f'https://www.daraz.pk/catalog/?_keyori=ss&from=input&page={i}&q=iphone&spm=a2o2r4.tm80022604.search.go.45b4986bKKlnjZ'
            yield SeleniumRequest(
                url = absolute_url,
                wait_time=  5,
                callback= self.parse
            )
       
        

