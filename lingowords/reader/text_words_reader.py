from lingowords.reader.words_reader import WordsReader


class TextWordReader(WordsReader):

    def parse(self, words):
        # Parse the wordlist
        word_list = words.split("\n")
        # Loop over all the words
        for word in word_list:
            if self.validate(word):  # If the word is valid
                self.words.append(word)  # Append the word to the list
        return self.words
