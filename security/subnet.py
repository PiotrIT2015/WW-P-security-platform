"""
Subnet Calculator
"""


import ipaddress



class SubnetCalculator:



    def calculate(
            self,
            ip,
            mask
    ):


        network = ipaddress.ip_network(

            f"{ip}/{mask}",

            strict=False

        )


        return {


            "network":

            str(network.network_address),



            "broadcast":

            str(network.broadcast_address),



            "hosts":

            network.num_addresses - 2

        }