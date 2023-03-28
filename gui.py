class GUI:

    def __init__(self):
        with open("title.txt", "r", encoding="utf-8") as f:
            print(f.read() + "\n1. PLAY \n2. GAME MODE \n3. HOW TO PLAY")
        with open("floppatest.txt", "r", encoding="utf-8") as g:
            print(g.read()) #print big floppa en ascii, on peut remplacer plus tard par mrincredible

        choix = input("le choix")
    
        if choix == "1":
            print("le jeu gaming")

        elif choix == "2":
            print("1.NOMBRE DE JOUEURS ([1])([2]) \n2.DIFFICULTE ([1])([2])([3]) \nMODE INCREDIBLE ([n])([y])")

            choix_gm = input("(1/2/3)")

            bruh = "#dilexyies"
            players = 1
            difficulty = 2
            incredible_mode = "n"

            if choix_gm == "1":
                n_players = input("nombre de joueurs (1/2)?")

            if n_players == "1" or "2":
                players = n_players
            else:
                players = players
                print(bruh)

            if choix_gm == "2":
                n_difficulty = input("difficulté des mots? (1/2/3)")
                if n_difficulty == "1" or "2" or "3":
                    difficulty = n_difficulty
                else:
                    difficulty = difficulty
                    print(bruh)
                








        elif choix == "3":
            print("la honte il sait pas comment jouer")
        else:
            print("soulja boy est le premier rappeur avec un iphone")

    


        
ok = GUI()


    