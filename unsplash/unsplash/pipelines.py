# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

from scrapy.pipelines.images import ImagesPipeline


class UnsplashPipeline:
    @staticmethod
    def process_item(item, spider):
        return item


class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return item['file_path'][0]
