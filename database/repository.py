"""
Repository
"""

import mysql.connector

from core.config import DATABASE


class Repository:

    @staticmethod
    def save_search(

        url,

        keyword,

        results,

        sentiment

    ):

        conn = mysql.connector.connect(

            **DATABASE

        )

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO search_results

            (

                url,

                keyword,

                results,

                sentiment

            )

            VALUES

            (

                %s,

                %s,

                %s,

                %s

            )

            """,

            (

                url,

                keyword,

                results,

                sentiment

            )

        )

        conn.commit()

        cursor.close()

        conn.close()