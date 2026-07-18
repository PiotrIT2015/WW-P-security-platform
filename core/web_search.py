"""
White Dwarf Search Engine
Backend
"""

from bs4 import BeautifulSoup
import requests


class WebSearcher:

    def __init__(self, timeout=10):
        self.timeout = timeout

    def search(self, url: str, phrase: str):

        if not url:
            return False, "Empty URL"

        if not phrase:
            return False, "Empty phrase"

        try:

            response = requests.get(
                url,
                timeout=self.timeout,
                headers={
                    "User-Agent":
                        "Mozilla/5.0"
                }
            )

            response.raise_for_status()

        except Exception as e:

            return False, str(e)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        paragraphs = soup.find_all("p")

        results = []

        phrase = phrase.lower()

        for paragraph in paragraphs:

            text = paragraph.get_text(
                " ",
                strip=True
            )

            if phrase in text.lower():

                results.append(text)

        if not results:

            return True, "No results."

        return True, "\n\n".join(results)