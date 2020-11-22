import scrapy
from book.items import BookItem
from scrapy.loader import ItemLoader


class BscrapeSpider(scrapy.Spider):
    name = 'bscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        for article in  response.xpath("//article[@class = 'product_pod']"):
            loader = ItemLoader(item = BookItem(), selector= article)
            img_link = article.xpath(".//div[@class = 'image_container']/a/img/@src").get()
            absolute_url = response.urljoin(img_link)
            loader.add_value('image_urls', absolute_url)
            loader.add_xpath('book_name', './/h3/a/@title')

            yield loader.load_item() 

            
