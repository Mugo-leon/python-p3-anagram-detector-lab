# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Convert the input word to lowercase for case-insensitive comparison
        word = self.word

        # Filter the word_list to get only the anagrams
        anagrams = [candidate for candidate in word_list if self.is_anagram(word, candidate)]

        return anagrams

    def is_anagram(self, word, candidate):
        # Helper function to check if two words are anagrams
        candidate_lower = ''.join(candidate).lower()  # Join the list to form a string before conversion
        word = sorted(word)
        candidate_lower = sorted(candidate_lower)

        return word == candidate_lower and self.word != candidate_lower


# Example usage:
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)

