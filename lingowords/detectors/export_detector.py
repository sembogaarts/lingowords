from lingowords.exporter.json_words_exporter import JsonWordsExporter
from lingowords.exporter.mysql_words_exporter import MysqlWordsExporter


class ExportDetector:

    def ask(self):
        # Show options to the user
        print("How would you like to export the words?")
        print("1. MySQL")
        print("2. JSON")
        option = int(input("#: "))
        # Check for importer
        return self.selectReader(option)

    def selectReader(self, i):
        switcher = {
            1: MysqlWordsExporter(),
            2: JsonWordsExporter()
        }
        return switcher.get(i, "Invalid option")