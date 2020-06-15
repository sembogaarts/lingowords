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

    def importWords(self):
        importer_detector = ImportDetector()
        importer = importer_detector.ask()
        importer.ask()
        words = importer.words()
        self.readWords(words)

    def readWords(self, words):
        #
        reader_detector = ReaderDetector()
        reader = reader_detector.ask()
        words = reader.parse(words)
        self.exportWords(words)

    def exportWords(self, words):
        print(words)
        export_detector = ExportDetector()
        export_class = export_detector.ask()
        exporter = export_class()

        try:
            exporter.store(words)
        except Exception as e:
            print(e)


main = Main()  # Start the script
