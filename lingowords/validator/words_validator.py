class WordsValidator:

    min_word_length = 4
    max_word_length = 7

    characters = (
        '-',
        ',',
        '.',
        '"',
        '\''
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
        if self.contains_digits(word):
            return False
        # Everything is good
        return True

    def is_lowercase(self, word):
        return all(c.islower() for c in word)

    def contains_digits(self, word):
        return any(c.isdigit() for c in word)

    def has_special_characters(self, word):
        return any((c in word) for c in self.characters)

    def is_correct_length(self, word):
        # Get length of the word
        length_of_word = len(word)
        # Perform the check
        return length_of_word >= self.min_word_length and length_of_word <= self.max_word_length

