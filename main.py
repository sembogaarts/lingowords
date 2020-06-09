from lingowords.importer.file_words_importer import FileWordsImporter
from lingowords.importer.url_words_importer import UrlWordsImporter
from lingowords.reader.words_reader import WordsReader
from lingowords.detectors.type_detector import TypeDetector

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

        self.fetchWords(importer)

    def selectImporter(self, i):
        switcher = {
            1: UrlWordsImporter,
            2: FileWordsImporter
        }
        return switcher.get(i, "Invalid option")

    def fetchWords(self, importer_class):
        # Initialize the given class
        importer = importer_class()
        # Asks the user for class specific input
        importer.ask()
        # Try to get the words from source
        try:
            words = importer.words()  # Get the words
            self.importWords(words)  # Parse the words
        except FileNotFoundError:
            print('File not found.')

    def importWords(self, words):

        typeDetector = TypeDetector()

        reader = typeDetector.ask()

        words = reader.parse(words)

        print(words)
        pass


main = Main()  # Start the script
