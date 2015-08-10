''' defines the data on records to collect '''
import scrapy

class RecordItem(scrapy.Item):
    ''' metadata on a record (as in a cut disc of vinyl) '''
    catalog_num = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
