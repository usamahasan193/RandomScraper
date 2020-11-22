import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
        items = response.xpath("//td[@class = 'titleColumn']")
        for item in items:
            title = item.xpath(".//a/text()").get()
            
            link = item.xpath(".//a/@href").get()
            abolute_url = response.urljoin(link)

            yield {
                'title': title,
                'Link': abolute_url
            }
