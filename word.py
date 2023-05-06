import json
from random import choice

class WORD:
    def get_word(self, difficulte):
        with open("ressources/words.json", "r") as f:
            words = json.load(f)

        word_range = words[difficulte]
        word_choice = choice(list(word_range.items()))

        self.word_list = [i for i in word_choice[0]]

        return self.word_list, word_choice[1]
    
    # plus besoin
    def word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.LEAST_USED_LETTERS:
                bonus += 2

        return lenght + bonus

    def check_win(self, guesses):
        return all(i in guesses for i in self.word_list)