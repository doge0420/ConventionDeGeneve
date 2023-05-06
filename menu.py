import sys
from leaderboard import LEADERBOARD
from gui import GUI

class MENU(GUI):
    def __init__(self):
        self.choice = {"joueurs" : 1, "difficulte" : "1", "mode_incredible" : False, "pseudo" : None}
        self.flag = True

        self.leaderboard = LEADERBOARD()

    # debug
    def __del__(self):
        print(self.choice)

    # menu
    ############################

    def menu(self):
        # ascii
        self.load_ascii()

        # ask pseudo
        self._ask_pseudo()

        # loop du choix
        self._choice_loop()
        
        return self.choice

    def _ask_pseudo(self):
        pseudo = input("Quel est votre pseudo ? : ")
        self.choice["pseudo"] = pseudo

    def _choice_loop(self):
        while self.flag:
            self.refresh_screen_menu()
            self._get_choice()

    def _get_choice(self):
        choice = input("1. PLAY \n2. SETTINGS \n3. HOW TO PLAY\n4. SCOREBOARD\n5. EXIT\n\nVotre choix : ")

        if choice == "1":
            self.flag = False

        elif choice == "2":
            self.refresh_screen_menu()
            self._get_settings()

        elif choice == "3":
            self.refresh_screen_menu()
            with open("ressources/help.txt", "r", encoding="utf-8") as f:
                print(f.read())
            input("\nAppuyez sur entrer pour continuer...")
        
        elif choice == "4":
            self.refresh_screen_menu()
            self.leaderboard.show_scoreboard()
            input("\nAppuyez sur entrer pour continuer...")
        
        elif choice == "5":
            sys.exit("\nA la prochaine !")
        
        else:
            print("\nNumero invalide\n")

    def _get_settings(self):
        setting = input("1.NOMBRE DE JOUEURS ([1])([2]) \n2.DIFFICULTE ([1])([2])([3]) \n3.MODE INCREDIBLE ([n])([y])\n4.ARRIERE\n\nChoix du reglage : ")

        if setting == "1":
            n_players = input("Nombre de joueurs (1/2)? : ")

            if n_players == "1" or "2":
                self.choice["joueurs"] = n_players
            else:
                print("#dilexyies")

        elif setting == "2":
            n_difficulty = input("difficulté des mots (1/2/3)? : ")
            if n_difficulty == "1" or "2" or "3":
                self.choice["difficulte"] = n_difficulty
            else:
                print("#dilexyies")

        elif setting == "3":
            choice = input("(y/n) ? : ")
            
            if choice == "y":
                self.choice["mode_incredible"] = True
            elif choice == "n":
                self.choice["mode_incredible"] = False
            else:
                print("#dilexyies")

        elif setting == "4":
            self.refresh_screen_menu()
            self._get_choice()

        else:
            print("\nNumero invalide\n")
    
    # jeu
    ############################
        
    def display_word_guess(self, word : list, guesses : list, bad_guesses : list, word_diff : int):
        self.clear_screen()

        print("\n\n\n")

        print(f"\tMot à deviner : \t", end="")

        for word_letter in word:
            if word_letter in guesses:
                print(word_letter, end="")
            else:
                print(".", end="")

        print("\n\n")

        print(f"\tDifficulté : \t{word_diff}", end="")

        print("\n\n")

        print("\tLettres fausses : \t", end="")

        for bad_guess in bad_guesses:
            print(f"{bad_guess}", end=" ")

        print("\n\n\n")

if __name__ == "__main__": 
    menu = MENU()