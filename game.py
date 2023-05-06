from encodings import utf_8
from gui import GUI
from random import choice
from string import ascii_lowercase, ascii_uppercase
from time import sleep
from PIL import Image

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

        self.clear_screen()
        self.display_word_guess(word_list, self.guesses, self.bad_guess, word_diff)
        guess_input = input("Veuillez choisir une lettre : ")

        while self.run:
            if len(guess_input) == 1 and (guess_input in ascii_lowercase or guess_input in ascii_uppercase):
                guess_input = guess_input.lower()
                if guess_input in word_list:
                    self.guesses.append(guess_input)
                    
                    # debug
                    # print(self.guesses)
                    # print(word_list)
                    # print(self.check_win(word_list))
                    
                    print("Bonne lettre :)")

                    # win
                    if self._check_win(word_list) and (len(set(word_list)) == len(set(self.guesses))):  
                        self.clear_screen()
                        self.run = False
                        
                        self.win_screen(word_list, word_diff, self.bad_guess, self.choice["pseudo"])
                        
                        if self.choice["mode_incredible"]:
                            self._mode_incredible(True)

                else:
                    self.bad_guess.append(guess_input)
                    self.clear_screen()
                    
                    print("Mauvaise lettre :(")

                    if len(self.bad_guess) > 11:
                        self.run = False
                        ... # death screen
                    elif self.choice["mode_incredible"]:
                        self._mode_incredible()
                    else:
                        self._mode_normal()
            else:
                print("Veuillez entrez UNE L-E-T-T-R-E.")

            sleep(1.5)

            if self.run:
                self.clear_screen()
                self.display_word_guess(word_list, self.guesses, self.bad_guess, word_diff)
                guess_input = input("Veuillez choisir une lettre : ")

    def _check_win(self, word_list):
        return all(i in self.guesses for i in word_list)

    def _mode_incredible(self, win=False):
        if win:
            with Image.open("ressources/incredible/mincredible_bravo.png") as f:
                f.show()
        else:
            with Image.open(f"ressources/incredible/mincredible{len(self.bad_guess)}.png") as f:
                f.show()
            
    def _mode_normal(self):
        print("\n\n")
        with open (f"ressources/pendus11/pendu{len(self.bad_guess)}.txt", "r", encoding="utf-8") as f:
            print(f.read())

if __name__ == "__main__":
    GAME()