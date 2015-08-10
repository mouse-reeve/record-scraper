''' defines the data on records to collect '''
import scrapy

class RecordItem(scrapy.Item):
    ''' metadata on a record (as in a cut disc of vinyl) '''
    artist = scrapy.Field()
    title = scrapy.Field()
    genre = scrapy.Field()
    style = scrapy.Field()
