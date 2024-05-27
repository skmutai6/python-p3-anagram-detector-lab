# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list): # Initialize an empty list to store the matching words
        matching = []

        matching = [word for word in word_list if sorted(self.word) == sorted(word)]

        return matching
    