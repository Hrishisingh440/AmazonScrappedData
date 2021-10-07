import scrapy
from ..items import AmazondataItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    pagenumber=2

    start_urls = ['http://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1633639186&rnid=2684818031&ref=lp_976390031_nr_p_n_publication_date_0']

    def parse(self, response):
        items=AmazondataItem()
        title=response.css('.a-color-base.a-text-normal').css('::text').extract()
        author = response.css('.a-color-base.a-text-normal').css('::text').get()
        price = response.css('.a-price-whole::text').get()
        image_link= response.css('.s-prefetch-image::attr(src)').getall()

        items['title']=title
        items['author'] = author
        items['price'] = price
        items['image_link'] = image_link

        yield items
        next_page='https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page='+str(AmazonSpiderSpider.pagenumber)+'&qid=1633641480&rnid=2684818031&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number<=1001:
            AmazonSpiderSpider.pagenumber+=1
            yield response.follow(next_page,callback=self.parse)






