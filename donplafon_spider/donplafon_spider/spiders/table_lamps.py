import scrapy

class TableLampsSpider(scrapy.Spider):
    name = 'table_lamps'
    allowed_domains = ['donplafon.ru']
    start_urls = ['https://donplafon.ru/catalog/nastolnye/']

    def parse(self, response):
        for product in response.css('div.itemtype="https://schema.org/Product"'):
            yield {
                'title': product.css('class="productItem__title"').get().strip(),
                'price': product.css('class="productItem__cost"').get().strip(),
                'link': response.urljoin(product.css('class="productItem__href"').get())
            }

        next_page = response.css('a.page-next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
