
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
    xpath_fields = {
        'sku': '/html/head/meta[11]/@content',
    }

    
# <meta property="product:retailer_item_id" content="SKU1108">