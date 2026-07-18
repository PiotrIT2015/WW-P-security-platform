"""
WW-P Security Platform
Web Search Service
"""

import requests
from bs4 import BeautifulSoup


class WebSearchService:

    @staticmethod
    def search(url: str, keyword: str):

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for paragraph in soup.find_all("p"):

            text = paragraph.get_text(" ", strip=True)

            if keyword.lower() in text.lower():
                results.append(text)

        return results