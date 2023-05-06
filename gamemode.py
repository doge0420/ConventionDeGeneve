from PIL import Image

class GAMEMODE:
    
    # mode incredible
    ############################
    def pendu_incredible(self, bad_guess):
        """
        prends le nombre de fausses lettres et affiche l'image correspondante
        """
        with Image.open(f"ressources/incredible/mincredible{len(bad_guess)}.png") as f:
            f.show()

    def bravo_incredible(self):
        """
        affiche une image pour féliciter l'utilisateur
        """
        with Image.open("ressources/incredible/mincredible_bravo.png") as f:
            f.show()

    # mode normal
    ############################
    def pendu_normal(self, bad_guess):
        """
        prends le nombre de fausses lettres et affiche le stage pendu en ascii qui y correspond
        """
        print("\n\n")
        with open (f"ressources/pendus11/pendu{len(bad_guess)}.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    def bravo_normal(self):
        """
        félicite l'utilisateur, affiche win.txt
        """
        with open("ressources/win.txt", "r", encoding="utf-8") as f:
            print(f.read())