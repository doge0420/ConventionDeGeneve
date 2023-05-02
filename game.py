from encodings import utf_8
from gui import GUI
from random import choice
from string import ascii_lowercase, ascii_uppercase
from time import sleep

class GAME(GUI):
    def __init__(self):
        super().__init__()

        self.LEAST_USED_LETTERS = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
        self.run = True
        self.guesses = []
        self.bad_guess = []

        self.menu()

        self.game_loop()

    def _choose_word(self, debug = False):
        with open("ressources/words.txt", "r") as f:
            words = f.readlines()

        word = choice(words).strip()

        if debug:
            print(word)

        return [i for i in word]

    def _word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.LEAST_USED_LETTERS:
                bonus += 2

        return lenght + bonus

    def game_loop(self):
        word_list = self._choose_word()

        word_diff = self._word_difficulty(word_list)

        while self.run:
            self.clear_screen()
            self.display_word_guess(word_list, self.guesses, self.bad_guess, word_diff)

            guess_input = input("Veuillez choisir une lettre : ")

            if len(guess_input) == 1 and (guess_input in ascii_lowercase or guess_input in ascii_uppercase):
                guess_input = guess_input.lower()
                if guess_input in word_list:
                    self.guesses.append(guess_input)
                    print("Bonne lettre :)")
                else:
                    self.bad_guess.append(guess_input)
                    self.clear_screen()
                    print("Mauvaise lettre :(")
                    print("\n\n")
                    with open (f"pendus11/pendu{len(self.bad_guess)}.txt", "r", encoding="utf-8") as f:
                        print(f.read())
            else:
                print("Veuillez entrez UNE L-E-T-T-R-E.")

            sleep(1.5)

if __name__ == "__main__":
    GAME()