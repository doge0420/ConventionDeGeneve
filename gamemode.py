from PIL import Image

class GAMEMODE:
    
    # mode incredible
    ############################
    def pendu_incredible(self, bad_guess):
        with Image.open(f"ressources/incredible/mincredible{len(bad_guess)}.png") as f:
            f.show()

    def bravo_incredible(self):
        with Image.open("ressources/incredible/mincredible_bravo.png") as f:
            f.show()

    # mode normal
    ############################
    def pendu_normal(self):
        print("\n\n")
        with open (f"ressources/pendus11/pendu{len(self.bad_guess)}.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def bravo_normal(self):
        with open("ressources/win.txt", "r", encoding="utf-8") as f:
            print(f.read())