from gui import GUI
from random import choice
from itertools import repeat

class PARTIES(GUI):
    def __init__(self):
        super().__init__()
        
        self.LEAST_USED_LETTERS = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
        
        self.menu()
        
        self.display_word_guess(self._choose_word())
        
    def _choose_word(self, debug = False):
        with open("words.txt", "r") as f:
            words = f.readlines()

        word = choice(words).strip()

        self._word_preprocess(word)

        if debug:
            print(word)

        return word

    def _word_preprocess(self, word):
        key = [i for i in word] # conversion du mot en liste de lettres
        values = repeat(False, len(word))
        
        self.word_dict = dict(zip(key, values))

    def _word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.LEAST_USED_LETTERS:
                bonus += 2

        return lenght + bonus

    def display_word_guess(self, word):
        self.clear_screen()
        
        res = ""
        for letter in self.word_dict.keys():
            if self.word_dict[letter]:
                res += letter + " "
            else:
                res += "_ "

        print(f"\n\n{res}\n\n")

if __name__ == "__main__":
    PARTIES()