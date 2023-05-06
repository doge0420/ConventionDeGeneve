import os

class GUI:
    @staticmethod
    def clear_screen():
        if os.name == "nt": #windows
            os.system("cls")
        elif os.name == "posix": #linux && mac
            os.system("clear")
        else:
            print("OS non supporté")

    def load_ascii(self):
        with open("ressources/title.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def refresh_screen_menu(self):
        self.clear_screen()
        self.load_ascii()