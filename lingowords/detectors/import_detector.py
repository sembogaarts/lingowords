from lingowords.importer.file_words_importer import FileWordsImporter
from lingowords.importer.url_words_importer import UrlWordsImporter


class ImportDetector:

    def ask(self):
        # Show options to the user
        print("Lingowords")
        print("1. Importeren met URL")
        print("2. Bestand importeren")
        # Ask the user for input
        option = int(input("#: "))
        # Check for importer
        return self.selectImporter(option)

    def selectImporter(self, i):
        switcher = {
            1: UrlWordsImporter,
            2: FileWordsImporter
        }
        return switcher.get(i, "Invalid option")