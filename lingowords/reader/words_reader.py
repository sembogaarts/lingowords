import abc
from lingowords.validator.words_validator import WordsValidator


class WordsReader:

    words = []
    validator = WordsValidator()

    def validate(self, word):
        return self.validator.validate(word)

    @abc.abstractmethod
    def parse(self, words):
        raise NotImplementedError('users must define `parse` to use this base class')