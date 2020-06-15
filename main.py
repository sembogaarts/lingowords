from lingowords.detectors.import_detector import ImportDetector
from lingowords.detectors.export_detector import ExportDetector
from lingowords.detectors.reader_detector import ReaderDetector
from dotenv import load_dotenv


class Main:

    def __init__(self):
        # Load Enviroment
        load_dotenv()
        # Import Words
        self.importWords()

    #
    # Imports the word with selected importer
    #
    def importWords(self):
        importer_detector = ImportDetector()
        importer_class = importer_detector.ask()
        importer = importer_class()
        importer.ask()
        words = importer.words()
        self.readWords(words)

    #
    # Reads all the words in the file
    #
    def readWords(self, words):
        reader_detector = ReaderDetector()
        reader_class = reader_detector.ask()
        reader = reader_class()
        words = reader.parse(words)
        self.exportWords(words)

    #
    # Exports all the words
    #
    def exportWords(self, words):
        export_detector = ExportDetector()
        export_class = export_detector.ask()
        exporter = export_class()
        exporter.store(words)


main = Main()  # Start the script
