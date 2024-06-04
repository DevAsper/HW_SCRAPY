import scrapy


class TableLampsSpider(scrapy.Spider):
    name = 'table_lamps'
    allowed_domains = ['donplafon.ru']
    start_urls = ['https://donplafon.ru/catalog/nastolnye/']

    def parse(self, response):
        for product in response.css('div.id="product-list"'):

            title = product.css('div.data-name::text').get()
            if title:
                title = title.strip()

            price = product.css('div.data-price::text').get()
            if price:
                price = price.strip()

            link_element = product.css('a.itemprop="url"::attr(href)').get()
            if link_element:
                link = response.urljoin(link_element.strip())
            else:
                link = None


            if title and price and link:
                yield {
                    'title': title,
                    'price': price,
                    'link': link
                }


        next_page = response.css('a.page-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
