import mysql.connector

from core.config import DATABASE

from core.logger import get_logger

logger = get_logger("database")


def initialize_database():

    connection = None

    cursor = None

    try:

        connection = mysql.connector.connect(

            host=DATABASE.host,

            user=DATABASE.user,

            password=DATABASE.password,

            database=DATABASE.database,

            port=DATABASE.port,

            connect_timeout=5

        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS search_results(

                id INT AUTO_INCREMENT PRIMARY KEY,

                url TEXT,

                query TEXT,

                result LONGTEXT,

                sentiment VARCHAR(64),

                timestamp TIMESTAMP
                DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        connection.commit()

        logger.info("Database initialized.")

    except mysql.connector.Error as e:

        logger.error(e)

    finally:

        if cursor:

            cursor.close()

        if connection:

            connection.close()