"""
Shodan launcher
"""

import webbrowser


class ShodanLauncher:

    URL = "https://www.shodan.io"

    @staticmethod
    def open():

        webbrowser.open(
            ShodanLauncher.URL
        )