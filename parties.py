from gui import GUI
from random import choice

class PARTIES:
    def __init__(self, gui):
        self.LEAST_USED_LETTERS = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
        self.gui = gui # attend que le joueur choisisse play
        self.choice = self.gui.menu()
        self.gui.display_word_guess(self._choose_word())

    # en cours
    def _word_process(self, word):
        self.letter_list = list(word)
        self.guess_list = ["-" * len(word)] # guess_list generation
        
    def _choose_word(self, debug = False):
        with open("words.txt", "r") as f:
            words = f.readlines()

        word = choice(words).strip()

        if debug:
            print(word)

        return word

    def _word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.LEAST_USED_LETTERS:
                bonus += 2

        return lenght + bonus

if __name__ == "__main__":
    gui = GUI()

    PARTIES(gui)