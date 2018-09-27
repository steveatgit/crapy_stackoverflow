# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StackoverflowPipeline(object):
    def open_spider(self, spider):
        print "open spider..."

    def close_spider(self, spider):
        print "close spider..."

    def process_item(self, item, spider):
        link = item['link']
        file_name = link.replace('/', '_').replace(':', '_')
        fp = open('result/' + file_name, 'w')
        fp.write(item['body'])
        fp.close()
        return item
