from lingowords.exporter.json_words_exporter import JsonWordsExporter
from lingowords.exporter.mysql_words_exporter import MysqlWordsExporter


class ExportDetector:

    def ask(self):
        # Show options to the user
        print("How would you like to export the words?")
        print("1. MySQL")
        print("2. JSON")
        # Ask the user for input
        option = input("#: ")
        # Check type
        if option.isdigit():
            option = int(option)
        else:
            print("[ERROR] Wrong input")
            self.ask()
        # Check for importer
        return self.selectReader(option)

    def selectReader(self, i):
        switcher = {
            1: MysqlWordsExporter,
            2: JsonWordsExporter
        }
        # Check if the option exists
        switch_class = switcher.get(i)
        # Check if instance exists
        if switch_class:
            return switch_class
        else:
            print("[ERROR] Invalid option")
            self.ask()