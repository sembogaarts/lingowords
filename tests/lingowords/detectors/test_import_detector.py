import unittest
from unittest.mock import patch
from lingowords.detectors.import_detector import ImportDetector
from lingowords.importer.file_words_importer import FileWordsImporter
from lingowords.importer.url_words_importer import UrlWordsImporter


class TestImportDetector(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask_mysql(self, input):
        # Creates a new import detector
        impport_detector = ImportDetector()
        # Chose for MySQL
        url_importer = impport_detector.ask()
        self.assertEqual(url_importer, UrlWordsImporter)

    @patch('builtins.input', return_value='2')
    def test_ask_json(self, input):
        # Creates a new import detector
        impport_detector = ImportDetector()
        # Chose for MySQL
        file_importer = impport_detector.ask()
        self.assertEqual(file_importer, FileWordsImporter)