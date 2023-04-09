class GUI:
    def __init__(self):
        self.choice = {"joueurs" : 1, "difficulte" : 1, "mode_incredible" : False, "pseudo" : None}
        self.flag = True

    # debug
    # def __del__(self):
    #     print(self.choice)

    def menu(self):
        # ascii
        self._load_ascii()

        # ask pseudo
        self._ask_pseudo()

        # loop du choix
        self._choice_loop()
        
        return self.choice

    def _ask_pseudo(self):
        pseudo = input("Quel est votre pseudo ? : ")
        self.choice["pseudo"] = pseudo

    def _load_ascii(self):
        with open("title.txt", "r", encoding="utf-8") as f:
            print(f.read())

    def _choice_loop(self):
        while self.flag:
            self._get_choice()

    def _get_choice(self):
        choice = input("1. PLAY \n2. SETTINGS \n3. HOW TO PLAY\nVotre choix : ")

        if choice == "1":
            ... # lance le jeu
            self.flag = False

        elif choice == "2":
            self._get_settings()

        elif choice == "3":
            ... # print un document qui aide
        
        else:
            print("\nNumero invalide\n")

    def _get_settings(self):
        setting = input("1.NOMBRE DE JOUEURS ([1])([2]) \n2.DIFFICULTE ([1])([2])([3]) \n3.MODE INCREDIBLE ([n])([y])\n4.ARRIERE\nChoix du reglage : ")

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
            self._get_choice()

        else:
            print("\nNumero invalide\n")

if __name__ == "__main__": 
    gui = GUI()