"""
Simple Web Crawler
"""


import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin



class WebCrawler:



    def crawl(
            self,
            url
    ):


        response = requests.get(

            url,

            timeout=10

        )


        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )


        links=[]


        for a in soup.find_all(
            "a",
            href=True
        ):


            links.append(

                urljoin(
                    url,
                    a["href"]
                )

            )


        return list(set(links))