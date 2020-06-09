from lingowords.reader.json_words_reader import JsonWordsReader
from lingowords.reader.text_words_reader import TextWordReader


class TypeDetector:

    def ask(self):
        # Show options to the user
        print("What is the type of the file?")
        print("1. Text")
        print("2. JSON")
        option = int(input("#: "))
        # Check for importer
        return self.selectReader(option)

    def selectReader(self, i):
        switcher = {
            1: TextWordReader(),
            2: JsonWordsReader()
        }
        return switcher.get(i, "Invalid option")