rm items.csv
source bin/activate
scrapy crawl discogs -o items.csv
deactivate
