"""
Website Crawler
"""

from urllib.parse import urljoin
from urllib.parse import urlparse

import requests

from bs4 import BeautifulSoup


class WebsiteCrawler:

    @staticmethod
    def crawl(url):

        headers = {

            "User-Agent":
            "Mozilla/5.0"

        }

        response = requests.get(

            url,

            headers=headers,

            timeout=10

        )

        response.raise_for_status()

        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )

        links = set()

        for a in soup.find_all("a", href=True):

            href = urljoin(url, a["href"])

            parsed = urlparse(href)

            if parsed.scheme and parsed.netloc:

                links.add(href)

        return sorted(list(links))