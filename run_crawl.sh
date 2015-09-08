file="items.json"
rm $file
source bin/activate
scrapy crawl discogs -o $file
deactivate
