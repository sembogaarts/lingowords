import abc


class WordsImporter:

    @abc.abstractmethod
    def ask(self):
        raise NotImplementedError('users must define `ask` to use this base class')

    @abc.abstractmethod
    def words(self):
        raise NotImplementedError('users must define `words` to use this base class')