file="items.json"
rm $file
source bin/activate
pip install -r requirements.txt
scrapy crawl discogs -o $file
deactivate
