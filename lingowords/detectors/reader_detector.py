from lingowords.reader.text_words_reader import TextWordReader


class ReaderDetector:

    def ask(self):
        # Show options to the user
        print("What is the type of the file?")
        print("1. Text")
        option = int(input("#: "))
        # Check for importer
        return self.selectReader(option)

    def selectReader(self, i):
        switcher = {
            1: TextWordReader
        }
        return switcher.get(i, "Invalid option")