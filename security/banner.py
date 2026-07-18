"""
Banner parser
"""

from typing import Dict


class BannerParser:

    @staticmethod
    def parse(service: Dict) -> str:

        product = service.get("product", "")
        version = service.get("version", "")
        extrainfo = service.get("extrainfo", "")

        parts = [
            product,
            version,
            extrainfo
        ]

        return " ".join(
            p for p in parts if p
        ).strip()

    @staticmethod
    def banner(script_data: Dict) -> str:

        return script_data.get(
            "banner",
            ""
        ).strip()