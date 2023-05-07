import sys
from leaderboard import LEADERBOARD
from gui import GUI

class MENU(GUI):
    def __init__(self):
        self.choice = {"joueurs" : 1, "difficulte" : "1", "mode_incredible" : False, "pseudo" : None}
        self.flag = True

        self.leaderboard = LEADERBOARD()

    def menu(self):
        """
        affiche le menu et retourne le choix de l'utilisateur.
        """
        self.clear_screen()
        
        # ascii
        self.print_ascii("ressources/title.txt")

        # ask pseudo
        self._ask_pseudo()

        # loop du choix
        self._choice_loop()
        
        return self.choice

    def _ask_pseudo(self):
        """
        demande à l'utilisateur son pseudo.
        """
        pseudo = input("Quel est votre pseudo ? : ")
        self.choice["pseudo"] = pseudo

    def _choice_loop(self):
        """
        boucle du menu.
        """
        while self.flag:
            self.refresh_screen_menu()
            self._get_choice()

    def _get_choice(self):
        """
        permet à l'utilisateur de choisir 5 options différentes, affichées en dessous de l'écran titre 
        1.PLAY, 2.SETTINGS, 3.HOW TO PLAY, 4.SCOREBOARD et 5.EXIT. 
        si l'utilisateur choisit : 
            1 (PLAY), le jeu commence
            2 (SETTINGS), _get_settings() est appelé
            3 (HOW TO PLAY), le text help.txt est affiché, renseignant le joueur de comment le jeu marche
            4 (SCOREBOARD), le scoreboard est affiché
            5 (EXIT), le jeu est fermé
        """
        num = input("1. PLAY \n2. SETTINGS \n3. HOW TO PLAY\n4. SCOREBOARD\n5. EXIT\n\nVotre choix : ")

        # PLAY
        if num == "1":
            self.flag = False

        # SETTINGS
        elif num == "2":
            self._get_settings()

        # HOW TO PLAY
        elif num == "3":
            self._help()
        
        # SCOREBOARD
        elif num == "4":
            self._show_leaderboard()
        
        # EXIT
        elif num == "5":
            sys.exit("\nA la prochaine !")

    def _get_settings(self):
        """
        affiche 3 paramètres, et l'option de retourner au menu, que l'utilisateur peux séléctionner avec un chiffre
        puis chaque paramètre est modifiable avec un chiffre, ou une lettre.
        """
        self.refresh_screen_menu()
        
        setting = input("1.NOMBRE DE JOUEURS ([1])([2]) \n2.DIFFICULTE ([1])([2])([3]) \n3.MODE INCREDIBLE ([n])([y])\n4.ARRIERE\n\nChoix du reglage : ")

        # NOMBRE DE JOUEURS
        if setting == "1":
            n_players = input("Nombre de joueurs (1/2)? : ")
            
            if n_players == "1" or "2":
                self.choice["joueurs"] = n_players

        # DIFFICULTE
        elif setting == "2":
            n_difficulty = input("difficulté des mots (1/2/3)? : ")
            
            if n_difficulty in ["1", "2", "3" ]:
                self.choice["difficulte"] = n_difficulty

        # MODE INCREDIBLE
        elif setting == "3":
            choice = input("(y/n) ? : ")
            
            if choice == "y":
                self.choice["mode_incredible"] = True
            elif choice == "n":
                self.choice["mode_incredible"] = False

        # ARRIERE
        elif setting == "4":
            self.refresh_screen_menu()
            self._get_choice()

    def _help(self):
        self.refresh_screen_menu()
        self.print_ascii("ressources/help.txt")
        input("\nAppuyez sur entrer pour continuer...")

    def _show_leaderboard(self):
        self.refresh_screen_menu()
        self.leaderboard.show_scoreboard()
        input("\nAppuyez sur entrer pour continuer...")

    # debug
    # def __del__(self):
    #     print(self.choice)

if __name__ == "__main__": 
    menu = MENU()