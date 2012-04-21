#!/bin/bash 

pebble_url="http://www.kickstarter.com/projects/597507018/pebble-e-paper-watch-for-iphone-and-android"
while [ 1 ]; do
    echo $(date) $(python kickscraper.py $pebble_url)
    sleep 900
done
