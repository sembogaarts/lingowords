from lingowords.importer.file_words_importer import FileWordsImporter
from lingowords.importer.url_words_importer import UrlWordsImporter


class ImportDetector:

    def ask(self):
        # Show options to the user
        print("Lingowords")
        print("1. Importeren met URL")
        print("2. Bestand importeren")
        # Ask the user for input
        option = input("#: ")
        # Check type
        if option.isdigit():
            option = int(option)
        else:
            print("[ERROR] Wrong input")
            self.ask()
        # Check for importer
        return self.selectImporter(option)

    def selectImporter(self, i):
        switcher = {
            1: UrlWordsImporter,
            2: FileWordsImporter
        }
        # Check if the option exists
        switch_class = switcher.get(i)
        # Check if instance exists
        if switch_class:
            return switch_class
        else:
            print("[ERROR] Invalid option")
            self.ask()