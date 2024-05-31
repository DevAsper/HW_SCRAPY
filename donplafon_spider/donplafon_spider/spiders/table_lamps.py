import scrapy

class TableLampsSpider(scrapy.Spider):
    name = 'table_lamps'
    allowed_domains = ['donplafon.ru']
    start_urls = ['https://donplafon.ru/catalog/nastolnye-lampy/']

    def parse(self, response):
        for product in response.css('div.product-item'):
            yield {
                'title': product.css('a.product-title::text').get().strip(),
                'price': product.css('span.price::text').get().strip(),
                'link': response.urljoin(product.css('a.product-title::attr(href)').get())
            }

        next_page = response.css('a.page-next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
