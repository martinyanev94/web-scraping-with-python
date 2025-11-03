import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://example.com/books']

    def parse(self, response):
        for book in response.css('div.book'):
            title = book.css('h2.title::text').get()
            author = book.css('p.author::text').get()
            yield {'title': title, 'author': author}
