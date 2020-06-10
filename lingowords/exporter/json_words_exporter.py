from lingowords.exporter.words_exporter import WordsExporter
import json
import os


class JsonWordsExporter(WordsExporter):
    filename = "lingwords_export.json"
    path = "~/Desktop"

    def ask(self):
        # Show options to the user
        print("Path to store file (default: (~/Desktop))")
        path = input("Path: ")
        # If overwrite
        if path:
            self.path = os.path.join(path, self.filename)
        else:
            self.path = os.path.join(os.path.expanduser('~'), 'Desktop', self.filename)

    def store(self, words):
        # Ask the user where to store the file
        self.ask()
        # Create sample file
        file = open(self.path, 'w')  # Trying to create a new file or open one
        # Write all words
        y = json.dumps(words)

        file.write(y)

        file.close()
