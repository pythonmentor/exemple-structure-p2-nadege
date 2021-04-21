import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url):
    """
    Documentation
    """
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.content, "html.parser")