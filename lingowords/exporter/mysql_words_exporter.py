from lingowords.exporter.words_exporter import WordsExporter
import os
import mysql.connector


class MysqlWordsExporter(WordsExporter):

    cnx = None

    def __init__(self):
        self.createConnection()

    def createConnection(self):
        try:
            # Open connection to the database
            self.cnx = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                database=os.getenv("MYSQL_DATABASE"),
                user=os.getenv("MYSQL_USERNAME"),
                password=os.getenv("MYSQL_PASSWORD")
            )
        except Exception as e:
            print("Error connecting to MySQL, check config")

    def store(self, words):
        # Open a new cursor to the database
        cursor = self.cnx.cursor(prepared=True)
        # Define the query
        query = "INSERT INTO words (word, length) VALUES (%s, %s)"
        # Use optimized loop for importing
        cursor.executemany(query, words)
        # Close the cursor
        cursor.close()
        # Commit the changes
        self.cnx.commit()
