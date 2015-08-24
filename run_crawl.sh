file="items.csv"
rm $file
source bin/activate
scrapy crawl discogs -o $file
deactivate
