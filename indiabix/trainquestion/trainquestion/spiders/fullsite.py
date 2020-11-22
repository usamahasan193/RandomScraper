import scrapy
import logging

class FullsiteSpider(scrapy.Spider):
    name = 'fullsite'
    allowed_domains = ['www.indiabix.com']
    start_urls = ['https://www.indiabix.com/aptitude/questions-and-answers/']

    def parse(self, response):
        items = response.xpath("//div[@class = 'div-topics-index']/ul/li")
        for item in items:
            title = item.xpath(".//a/text()").get()
            link = item.xpath(".//a/@href").get()
            complete_url = response.urljoin(link)
            yield response.follow(url = complete_url, callback= self.parse_content)
    
    def parse_content(self, response):
    
        tags = response.xpath("//div[@class = 'bix-div-container']")
        for tag in tags:
             title = tag.xpath(".//td[@class = 'bix-td-qtxt']/p/text()").get()
             option = tag.xpath(".//td[@class = 'bix-td-option']/text()").getall()
             answer = tag.xpath(".//span[@class = 'jq-hdnakqb mx-bold']/text()").get()

             yield {
             
             'question': title,
             'options': option,
             'answer': answer
             }    
        next_page = response.xpath("(//p[@class = 'mx-pager mx-lpad-25']//@href)[last()]").get()
        if(next_page):
            absolute_url = response.urljoin(next_page)
            yield response.follow(url = absolute_url, callback= self.parse_content)


        
