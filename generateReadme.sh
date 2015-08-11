echo "# record-scraper

Metadata about my [record collection](http://www.discogs.com/user/tripofmice/collection) crawled from Discogs

Top artists:
$( jq .[].artist items.json | sort | uniq -c | sort -r | head -3 | while read line; do
    echo "- $line"
done )

Top styles:
$( jq .[].style items.json | sort | uniq -c | sort -r | head -3 | while read line; do
    echo "- $line"
done )
" > README.md

