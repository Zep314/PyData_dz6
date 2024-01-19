from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..items import UnsplashItem
import os


class UnsplashImagesSpider(CrawlSpider):
    name = "unsplash_images"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]
    rules = (Rule(LinkExtractor(restrict_xpaths='//div[@class="pRk2s"]/ul/li/a'), follow=True),  # Переходы между темами
             Rule(LinkExtractor(restrict_xpaths='//div[@class="zmDAx"]/a'), callback="parse_item"),  #обработка страницы
             )

    @staticmethod
    def parse_item(response):
        item = {}
        categories = response.xpath('//a[@class="IQzj8 eziW_"]/text()').getall()

        try:
            # Убираем категорию Editorial (она не категория)
            categories.remove('Editorial')
        except ValueError:
            pass

        item['category'] = categories[0] if categories else 'None'
        item['name'] = response.xpath('//h1/text()').get()
        item['file_path'] = os.path.join(item['category'], f"{item['name']}.jpg")
        item['image_urls'] = response.xpath('//div[@class="MorZF"]/img/@src').get()

        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
        loader.add_value('name', item['name'],)
        loader.add_value('category', item['category'])
        loader.add_value('file_path', item['file_path'])
        loader.add_value('image_urls', item['image_urls'])

        yield loader.load_item()
