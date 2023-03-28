class GUI:

    def __init__(self):
        self.load_ascii()
    
    def load_ascii(self):
        with open("title.txt", "r", encoding="utf-8") as f:
            print(f.read())
        with open("floppatest.txt", "r", encoding="utf-8") as g:
            print(g.read()) #print big floppa en ascii, on peut remplacer plus tard par mrincredible

    def get_choice(self):
        choice = input("1. PLAY \n2. GAME MODE \n3. HOW TO PLAY\nVotre choix : ")

        if choice == "1":
            print("le jeu gaming")
            
            return None,None

        elif choice == "2":
            self.get_gamemode()

        elif choice == "3":
            print("la honte il sait pas comment jouer")

        return None,None

    # list[n_gamemode, parametre]
    def get_gamemode(self):
        gamemode = input("1.NOMBRE DE JOUEURS ([1])([2]) \n2.DIFFICULTE ([1])([2])([3]) \n3.MODE INCREDIBLE ([n])([y])\nChoix du gamemode : ")

        if gamemode == "1":
            n_players = input("Nombre de joueurs (1/2)? : ")

            if n_players == "1" or "2":
                players = n_players
            else:
                print("#dilexyies")
                
            return [1, players]

        if gamemode == "2":
            n_difficulty = input("difficulté des mots (1/2/3)? : ")
            if n_difficulty == "1" or "2" or "3":
                difficulty = n_difficulty
            else:
                print("#dilexyies")

            return [2, difficulty]

        if gamemode == "3":
            return [3, None]

if __name__ == "__main__": 
    ok = GUI()