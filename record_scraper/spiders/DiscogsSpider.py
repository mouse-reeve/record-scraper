''' crawls discogs.com for collection data '''
import scrapy

from record_scraper.items import RecordItem

class DiscogsSpider(scrapy.Spider):
    ''' defines spider '''
    name = "discogs"
    allowed_domains = ["discogs.com"]
    start_urls = ["http://www.discogs.com/user/tripofmice/collection"]

    def parse(self, response):
        ''' process links on collection page '''
        if 'tripofmice / Collection' in response.xpath('//title/text()').extract()[0]:
            for link in response.xpath('//a[contains(@href, "/release/")]/@href'):
                path = link.extract()
                yield scrapy.http.Request('http://www.discogs.com' + path)
            for link in response.xpath('//a[@class="pagination_next"]/@href'):
                path = link.extract()
                yield scrapy.http.Request('http://www.discogs.com' + path)

        item = RecordItem()

        try:
            header = response.xpath('//meta[@property="og:title"]/@content').extract()[0]
            item['artist'] = header.split(' - ')[0]
            item['title'] = header.split(' - ')[1]
            item['genre'] = response.xpath('//div[@itemprop="genre"]//a/text()').extract()[0]
            item['style'] = response.xpath('//a[contains(@href, "/style")]/text()').extract()
        except IndexError:
            pass

        if item:
            yield item
