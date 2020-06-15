import unittest
from unittest.mock import patch
from lingowords.exporter.json_words_exporter import JsonWordsExporter


class TestJsonWordsExporter(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask(self, input):
        exporter = JsonWordsExporter()
        exporter.ask()



