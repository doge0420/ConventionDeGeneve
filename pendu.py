from gui import GUI
from random import choice
from string import ascii_lowercase, ascii_uppercase
from time import sleep
import json
from gamemode import GAMEMODE



class PENDU(GUI,GAMEMODE):
    def __init__(self):
        super().__init__()

        self.LEAST_USED_LETTERS = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
        self.run = True
        self.guesses = []
        self.bad_guess = []
        
        self.word = WORD()

        self.menu()

        self.game_loop()

    def game_loop(self):
        word_list, word_diff = self.word.get_word(self.choice["difficulte"])

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
                    if self.word.check_win(self.guesses) and (len(set(word_list)) == len(set(self.guesses))):  
                        self.clear_screen()
                        self.run = False
                        
                        self.win_screen(word_list, word_diff, self.bad_guess, self.choice["pseudo"])
                        
                        if self.choice["mode_incredible"]:
                            self._mode_incredible(True)

                else:
                    self.bad_guess.append(guess_input)
                    self.clear_screen()
                    
                    print("\n\nMauvaise lettre :(")

                    if len(self.bad_guess) > 11:
                        self.run = False
                        self.lose_screen(word_list)
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

if __name__ == "__main__":
    PENDU()