from lingowords.importer.file_words_importer import FileWordsImporter
from lingowords.importer.url_words_importer import UrlWordsImporter
from lingowords.importer.words_importer import WordsImporter


class Main:

    def __init__(self):
        self.ask()

    def ask(self):
        # Show options to the user
        print("Lingowords")
        print("1. Importeren met URL")
        print("2. Bestand importeren")
        # Ask the user for input
        option = int(input("#: "))
        # Check for importer
        importer = self.selectImporter(option)

        self.importWords(importer)

    def selectImporter(self, i):
        switcher = {
            1: UrlWordsImporter,
            2: FileWordsImporter
        }
        return switcher.get(i, "Invalid option")

    def importWords(self, importerClass=WordsImporter):
        # Initialize the given class
        importer = importerClass()
        # Asks the user for class specific input
        importer.ask()


main = Main()
