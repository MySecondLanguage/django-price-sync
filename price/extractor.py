
import re
import csv
from html import unescape
import requests

from django_easy_scraper import scraper

class ScrapeElgiganten(scraper.Scraper):
    # More details can be found here: https://pypi.org/project/django-easy-scraper/
    regex_fields = {
        'price': "<meta\sitemprop\=\"price\"\scontent\=\"(\d+)\"\/\>",
        'sku': "sku :\s\"(\d+)\"",
        'title': "class\=\"product\-title\"\>([\d\w\s\"\%\&\$\(\)\-\@\;\:\/\"\ä\S]+)\<\/h1\>",
    }

    

class ScrapeTeknikhouse(scraper.Scraper):
    # More details can be found here: https://pypi.org/project/django-easy-scraper/
    regex_fields = {
        # 'price': "<meta\sproperty\=\"product\:sale\_price\:amount\"\scontent\=\"(\d+)\"\s\/\>",
        # 'sku': "<meta\sproperty\=\"product\:retailer\_item\_id\"\scontent\=\"([\d\w]+)\"\/\>",
        # 'title': "<meta\sproperty\=\"og\:title\"\scontent\=\"([\d\w\s\-\&\%\-\.\+\=\#\@\^\'\"\;\:\d\w]+)\/\>",
    }
