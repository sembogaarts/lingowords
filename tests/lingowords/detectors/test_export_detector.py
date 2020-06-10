import unittest
from unittest.mock import patch
from lingowords.detectors.export_detector import ExportDetector
from lingowords.exporter.json_words_exporter import JsonWordsExporter
from lingowords.exporter.mysql_words_exporter import MysqlWordsExporter


class TestExportDetector(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask_mysql(self, input):
        self.assertEqual(ExportDetector.ask(), MysqlWordsExporter)

