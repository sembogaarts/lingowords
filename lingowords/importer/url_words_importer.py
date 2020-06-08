from lingowords.importer.words_importer import WordsImporter
import requests


class UrlWordsImporter(WordsImporter):

    url = ''  # The URL for the request

    def ask(self):
        print('# USING: URL IMPORTER #')
        self.url = input('URL: ')

    def fetchFile(self):
        return requests.get(self.url)

    def words(self):
        # Get the file
        r = self.fetchFile()
        # Check if the file has been fetched
        if r.status_code != 200:
            raise Exception
