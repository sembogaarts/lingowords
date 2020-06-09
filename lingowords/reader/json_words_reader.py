from lingowords.reader.words_reader import WordsReader


class JsonWordsReader(WordsReader):

    def parse(self, words):
        raise NotImplementedError('users must define `parse` to use this base class')