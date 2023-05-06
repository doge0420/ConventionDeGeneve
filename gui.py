import os

class GUI:
    @staticmethod
    def clear_screen(): 
        """
        fonction qui vide le terminal 
        en vérifiant quel OS est utilisé, puis utilisant la commande adequate pour le vider
        """
        if os.name == "nt": #windows
            os.system("cls")
        elif os.name == "posix": #linux && mac
            os.system("clear")
        else:
            print("OS non supporté")

    def load_ascii(self):
        """
        ouvre le fichier title.txt (écran titre) et l'affiche dans le terminal
        """
        with open("ressources/title.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def refresh_screen_menu(self):
        """
        execute les deux fonctions précédentes
        """
        self.clear_screen()
        self.load_ascii()