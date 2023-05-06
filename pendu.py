from menu import MENU
from string import ascii_lowercase, ascii_uppercase
from time import sleep
from PIL import Image
from word import WORD

class PENDU(MENU):
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
        self._init_game_loop()

        while self.run:
            if len(self.guess_input) == 1 and (self.guess_input in ascii_lowercase or self.guess_input in ascii_uppercase):
                self.guess_input = self.guess_input.lower()
                if self.guess_input in self.word_list:
                    self.guesses.append(self.guess_input)

                    print("Bonne lettre :)")

                    # win
                    if self.word.check_win(self.guesses) and (len(set(self.word_list)) == len(set(self.guesses))):  
                        
                        self.clear_screen()
                        self.run = False
                        
                        self.win_screen(self.word_list, self.word_diff, self.bad_guess, self.choice["pseudo"])
                        
                        if self.choice["mode_incredible"]:
                            self._mode_incredible(True)

                else:
                    self.bad_guess.append(self.guess_input)
                    self.clear_screen()
                    
                    print("\n\nMauvaise lettre :(")

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
                self._display_game()

    def _display_game(self):
        self.clear_screen()
        self.display_word_guess(self.word_list, self.guesses, self.bad_guess, self.word_diff)
        self.guess_input = input("Veuillez choisir une lettre : ")

    def _init_game_loop(self):
        self.word_list, self.word_diff = self.word.get_word(self.choice["difficulte"])
        self._display_game()

class MODE:
    def __init__(self, mode):
        self.mode = mode

    # mode incredible
    ############################
    def _pendu_incredible(self, bad_guess):
        with Image.open(f"ressources/incredible/mincredible{len(bad_guess)}.png") as f:
            f.show()

    def _bravo_incredible(self):
        with Image.open("ressources/incredible/mincredible_bravo.png") as f:
            f.show()

    # mode normal
    ############################
    def _pendu_normal(self):
        print("\n\n")
        with open (f"ressources/pendus11/pendu{len(self.bad_guess)}.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def _bravo_normal(self):
        with open("ressources/win.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def bravo(self):
        ...
        
    def pendu(self):
        ...

if __name__ == "__main__":
    PENDU()