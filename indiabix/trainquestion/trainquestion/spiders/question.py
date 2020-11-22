import scrapy


class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['www.indiabix.com']

    def start_requests(self):
        yield scrapy.Request(url = 'https://www.indiabix.com/aptitude/problems-on-trains/', callback= self.parse, headers= {
            'User-Agent': 'Mozila/5.0 (linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36'
        })


    def parse(self, response):
        items = response.xpath("//div[@class = 'bix-div-container']")
        for item in items:
             title = item.xpath(".//td[@class = 'bix-td-qtxt']/p/text()").get()
             option = item.xpath(".//td[@class = 'bix-td-option']/text()").getall()
             answer = item.xpath(".//span[@class = 'jq-hdnakqb mx-bold']/text()").get()
             

             yield {
             'question': title,
             'options': option,
             'answer': answer,
             
             }   
         
        next_page = response.xpath("(//p[@class = 'mx-pager mx-lpad-25']//@href)[last()]").get()
        if(next_page):
            absolute_url = response.urljoin(next_page)
            yield scrapy.Request(url = absolute_url, callback= self.parse, headers= {
            'User-Agent': 'Mozila/5.0 (linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36'
        })


