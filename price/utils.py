import requests
import re
from . exceptions import InvalidDomainError


def get_page_content(url):
    response = requests.get(url)
    return response.text


def get_domain_name(url):
    domain_name_pat = re.compile(r'www\.([\w\d\s\-\.]+)\/')
    extract = domain_name_pat.findall(url)

    if len(extract) == 0:
        raise InvalidDomainError(url=url)
    else:
        return extract[0]
