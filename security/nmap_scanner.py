"""
Nmap scanner
"""

import nmap

from security.banner import BannerParser


class NmapScanner:

    def __init__(self):

        self.scanner = nmap.PortScanner()

    def scan(

        self,

        host,

        start_port,

        end_port

    ):

        port_range = f"{start_port}-{end_port}"

        self.scanner.scan(

            hosts=host,

            ports=port_range,

            arguments="-sV --script banner"

        )

        results = []

        if host not in self.scanner.all_hosts():

            return results

        for protocol in self.scanner[host].all_protocols():

            ports = self.scanner[host][protocol]

            for port in sorted(ports.keys()):

                service = ports[port]

                if service["state"] != "open":

                    continue

                item = {

                    "port": port,

                    "protocol": protocol,

                    "service": service.get(

                        "name",

                        ""

                    ),

                    "description":

                        BannerParser.parse(

                            service

                        ),

                    "banner":

                        BannerParser.banner(

                            service.get(

                                "script",

                                {}

                            )

                        )

                }

                results.append(

                    item

                )

        return results