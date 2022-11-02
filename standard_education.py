import scrapy
import pandas as pd
import numpy as np

class QuotesSpider(scrapy.Spider):
    name = "std_edu"
    start_urls = [
        'https://thestandard.co/tag/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2/',
    ]

    def parse(self, response):
        for quote in response.css('div.news-item'):
            yield {
                'title': quote.css('a::text').get(),
                'article': quote.css('div.desc::text').get()
            }

        next_page = response.css('a.nextpostslink').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        df = pd.DataFrame(zip(title.article), columns = ['Title','Article'])
        print(df)