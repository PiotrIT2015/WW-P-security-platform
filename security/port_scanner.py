"""
Simple TCP scanner
"""

import socket


class PortScanner:

    def scan_port(

        self,

        host,

        port,

        timeout=1

    ):

        sock = socket.socket(

            socket.AF_INET,

            socket.SOCK_STREAM

        )

        sock.settimeout(timeout)

        result = sock.connect_ex(

            (host, port)

        )

        sock.close()

        return result == 0