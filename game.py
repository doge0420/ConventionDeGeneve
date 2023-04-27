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
        with open("words.txt", "r") as f:
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
        
        while self.run:
            self.clear_screen()
            self.display_word_guess(word_list, self.guesses, self.bad_guess)

            guess_input = input("Veuillez choisir une lettre : ")
            
            if len(guess_input) == 1 and (guess_input in ascii_lowercase or guess_input in ascii_uppercase):
                guess_input = guess_input.lower()
                if guess_input in word_list:
                    self.guesses.append(guess_input)
                    print("Bonne lettre :)")
                else:
                    self.bad_guess.append(guess_input)
                    print("Mauvaise lettre :(")
            else:
                print("Veuillez entrez une lettre.")

            sleep(1.5)

if __name__ == "__main__":
    GAME()
    print("ok")