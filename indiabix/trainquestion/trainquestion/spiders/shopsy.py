import scrapy
from scrapy_selenium import SeleniumRequest

class ShopsySpider(scrapy.Spider):
    name = 'shopsy'
    
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://shopsy.pk/search?q=watch',
            wait_time=5,
            callback= self.parse
        )

    def parse(self, response):
        items = response.xpath("//div[@class = 'subitem_product']")
        for item in items:
            title = item.xpath(".//h4[@class = 'card_product__content_title card_product__content_title_small']/span/text()").get()
            store = item.xpath(".//p[@class = 'card_product__content_meta']/a/text()").get()
            link = item.xpath(".//a[@class= 'card_product__link']/@href").get()
            absolute_url = response.urljoin(link)
            price = item.xpath("normalize-space(.//h3/text())").get()

            yield {
                'Product_name': title,
                'Store_name': store,
                 'Link': absolute_url,
                 'Price': price          
            }
            #for next page 


            




