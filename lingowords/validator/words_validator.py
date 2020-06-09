class WordsValidator:

    min_word_length = 4
    max_word_length = 7

    characters = (
        '-',
        ',',
        '.'
    )

    def validate(self, word):
        # Check for correct length
        if not self.is_correct_length(word):
            return False
        # Check for special characters
        if self.has_special_characters(word):
            return False
        # Check for lowercase
        if not self.is_lowercase(word):
            return False
        # Everything is good
        return True

    def is_lowercase(self, word):
        if any(c.isupper() for c in word):
            return False
        else:
            return True

    def has_special_characters(self, word):
        if any((c in word) for c in self.characters):
            return True
        else:
            return False

    def is_correct_length(self, word):
        # Get length of the word
        length_of_word = len(word)
        # Perform the check
        return length_of_word < self.min_word_length or length_of_word > self.max_word_length

