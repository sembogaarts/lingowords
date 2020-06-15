import unittest
from unittest.mock import patch
from lingowords.detectors.reader_detector import ReaderDetector
from lingowords.reader.text_words_reader import TextWordReader
from lingowords.reader.json_words_reader import JsonWordsReader


class TestImportDetector(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask_mysql(self, input):
        # Creates a new reader detector
        reader_detector = ReaderDetector()
        # Chose for MySQL
        text_reader = reader_detector.ask()
        self.assertEqual(text_reader, TextWordReader)

    @patch('builtins.input', return_value='2')
    def test_ask_json(self, input):
        # Creates a new reader detector
        reader_detector = ReaderDetector()
        # Chose for MySQL
        json_reader = reader_detector.ask()
        self.assertEqual(json_reader, JsonWordsReader)