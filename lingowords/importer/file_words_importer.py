from lingowords.importer.words_importer import WordsImporter
from os import path

class FileWordsImporter(WordsImporter):

    path = ''  # The path for the file

    def ask(self):
        print('# USING: FILE IMPORTER #')
        self.path = input('PATH: ')
        print(self.path)

    def fileExists(self):
        return path.exists(self.path)

    def getFileContent(self):
        fp = open(self.path, "r")
        content = fp.read()
        fp.close()
        return content

    def words(self):
        # Get the file
        if not self.fileExists():
            raise FileNotFoundError('File does not exist')
        # Get content for the file
        content = self.getFileContent()
        return content

