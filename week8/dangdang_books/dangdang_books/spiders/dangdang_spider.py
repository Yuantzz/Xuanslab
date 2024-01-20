import scrapy
import json


class DangdangSpider(scrapy.Spider):
    name = 'dangdang_spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.00.00.00.00.00.html']

    def parse(self, response):
        books = response.css('.bang_list li')

        result = []

        for book in books:
            title = book.css('.name a::text').get()
            author = book.css('.publisher_info a::text').get()
            price = book.css('.price .price_n::text').get()

            result.append({
                'title': title,
                'author': author,
                'price': price,
            })

        # 将结果写入 JSON 文件
        with open('dangdang_books.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)

        # 返回结果
        return result
