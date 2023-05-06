from string import ascii_lowercase, ascii_uppercase
from time import sleep
from word import WORD
from menu import MENU
from gamemode import GAMEMODE

class PENDU(MENU):
    def __init__(self):
        super().__init__()

        self.LEAST_USED_LETTERS = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
        self.run = True
        self.guesses = []
        self.bad_guess = []
        
        self.word = WORD()
        self.gamemode = GAMEMODE()

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
                        self._win_screen()

                else:
                    self.bad_guess.append(self.guess_input)
                    self.clear_screen()
                    
                    print("\n\nMauvaise lettre :(")

                    if len(self.bad_guess) > 11:
                        self._lose_screen()
                    elif self.choice["mode_incredible"]:
                        self.gamemode.pendu_incredible(self.bad_guess)
                    else:
                        self.gamemode.pendu_normal()
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

    def _win_screen(self):
        self.clear_screen()
        self.run = False
        
        if self.choice["mode_incredible"]:
            self.gamemode.bravo_incredible()
        
        score = len(self.word_list) + self.word_diff - len(self.bad_guess)
        
        print(f"\nLe mot etait : {''.join(self.word_list)}")
        print(f"\nVotre score est {score} pts !")

        self.leaderboard.add_scoreboard(score, self.choice["pseudo"])
        
    def _lose_screen(self):
        self.run = False
        
        with open("ressources/lose.txt", "r", encoding="utf-8") as f:
            lose_char = f.read()

        print(lose_char)
        print(f"\nLe mot etait : {''.join(self.word_list)}")

if __name__ == "__main__":
    PENDU()