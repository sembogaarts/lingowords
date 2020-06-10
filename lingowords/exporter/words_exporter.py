import abc


class WordsExporter:

    @abc.abstractmethod
    def store(self, words):
        raise NotImplementedError('users must define `store` to use this base class')