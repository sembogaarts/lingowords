import unittest
from unittest.mock import patch
from lingowords.detectors.export_detector import ExportDetector
from lingowords.exporter.json_words_exporter import JsonWordsExporter
from lingowords.exporter.mysql_words_exporter import MysqlWordsExporter


class TestExportDetector(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask_mysql(self, input):
        # Creates a new export detecto
        export_detector = ExportDetector()
        # Chose for MySQL
        mysql_exporter = export_detector.ask()
        self.assertEqual(mysql_exporter, MysqlWordsExporter)

    @patch('builtins.input', return_value='2')
    def test_ask_json(self, input):
        # Creates a new export detecto
        export_detector = ExportDetector()
        # Chose for MySQL
        json_exporter = export_detector.ask()
        self.assertEqual(json_exporter, JsonWordsExporter)