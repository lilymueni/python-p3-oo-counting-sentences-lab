#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace commas with periods to simplify splitting
        temp_value = self.value.replace(',', '.')
        # Split the string into sentences using period as the separator
        sentences = temp_value.split('.')
        # Remove any empty strings resulting from splitting
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())  # Output: False
print(string.is_question())  # Output: False
print(string.is_exclamation())  # Output: True
print(string.count_sentences())  # Output: 3
