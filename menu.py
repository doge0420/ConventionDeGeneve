import sys
from leaderboard import LEADERBOARD
from gui import GUI

class MENU(GUI):
    def __init__(self):
        self.choice = {"joueurs" : 1, "difficulte" : "1", "mode_incredible" : False, "pseudo" : None}
        self.flag = True

        self.leaderboard = LEADERBOARD()

    # debug
    # def __del__(self):
    #     print(self.choice)

    def menu(self):
        # ascii
        self.load_ascii()

        # ask pseudo
        self._ask_pseudo()

        # loop du choix
        self._choice_loop()
        
        return self.choice

    def _ask_pseudo(self):
        """
        demande à l'utilisateur son pseudonyme et le met dans le dictionaire choice
        """
        pseudo = input("Quel est votre pseudo ? : ")
        self.choice["pseudo"] = pseudo

    def _choice_loop(self):
        """
        fonction qui continue à tourner jusqu'à que self.flag soit False 
        (quand l'utilisateur quitte le jeu)
        """
        while self.flag:
            self.refresh_screen_menu()
            self._get_choice()

    def _get_choice(self):
        """
        permet à l'utilisateur de choisir 5 options différentes, affichées en dessous de l'écran titre
        1.PLAY, 2.SETTINGS, 3.HOW TO PLAY, 4.SCOREBOARD and 5.EXIT. 
        si l'utilisateur choisit 1 (PLAY), self.flag devient False et le jeu commence
        s'il choisit 2 (SETTINGS), _get_settings() est instancié
        s'il choisit 3 (HOW TO PLAY), le text help.txt est affiché, renseignant le joueur de comment le jeu marche
        s'il choisit 4 (SCOREBOARD), le scoreboard est affiché
        s'il choisit 5 (EXIT), le jeu est fermé avec sys.exit
        
        """
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

if __name__ == "__main__": 
    menu = MENU()