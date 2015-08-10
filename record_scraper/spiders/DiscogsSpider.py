''' crawls discogs.com for collection data '''
import re
import scrapy

from record_scraper.items import RecordItem

class DiscogsSpider(scrapy.Spider):
    ''' defines spider '''
    name = "discogs"
    allowed_domains = ["discogs.com"]
    start_urls = ["http://www.discogs.com/user/tripofmice/collection"]

    def parse(self, response):
        ''' process links on collection page '''
        for link in response.xpath('//a/@href'):
            if re.match(r'*\/release\/\d*', link):
                print link
