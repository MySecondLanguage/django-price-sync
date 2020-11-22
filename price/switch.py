from . exceptions import NotListedDomainError, NotFoundError, SKUnProductNotMatchedError, DoesNotExistError, InvalidDomainError
from . utils import get_domain_name
import re

from price.models import Product

from . extractor import ScrapeElgiganten, ScrapeTeknikhouse

from django_easy_scraper import switch

from rest_framework.exceptions import APIException



class Switch(switch.BaseSwitch):
    # More details can be found here: https://pypi.org/project/django-easy-scraper/
    switcher = {
        'elgiganten.se': ScrapeElgiganten.regex_url_scraper,
        # 'teknikhouse.se': ScrapeElgiganten.regex_url_scraper,
    }




# Extract and populate
def extract_to_update(pk):
    try:
        product = Product.objects.get(pk=pk)
    except Exception:
        raise DoesNotExistError()
    response = Switch.get_data(url=product.url, raise_exception=False)
    if response['sku']:
        if response['sku'] == product.sku:
            product.extracted_price = response['price']
            product.title = response['title']
            product.save()
        else:
            raise SKUnProductNotMatchedError(url=product.url)
    else:
        raise APIException(response, 'Missing item')

    return response
