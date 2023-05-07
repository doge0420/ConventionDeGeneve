import os

class GUI:
    @staticmethod
    def clear_screen(): 
        """
        efface le terminal (independant de l'OS).
        """
        if os.name == "nt": #windows
            os.system("cls")
        elif os.name == "posix": #linux && mac
            os.system("clear")
        else:
            print("OS non supporté")

    def print_ascii(self, path):
        """
        affiche un ascii art dans le terminal.
        """
        with open(f"{path}", "r", encoding="utf-8") as f:
            print(f.read())
            
    def refresh_screen_menu(self):
        """
        execute les deux fonctions précédentes
        """
        self.clear_screen()
        self.print_ascii("ressources/title.txt")