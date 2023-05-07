from PIL import Image
from gui import GUI

class GAMEMODE(GUI):
    
    # mode incredible
    ############################
    def pendu_incredible(self, bad_guess):
        """
        affiche mr incredible en fonction du nombre de fausses lettres.
        """
        with Image.open(f"ressources/incredible/mincredible{len(bad_guess)}.png") as f:
            f.show()

    def bravo_incredible(self):
        """
        affiche une image de tragulus pour féliciter le joueur.
        """
        with Image.open("ressources/incredible/mincredible_bravo.png") as f:
            f.show()

    # mode normal
    ############################
    def pendu_normal(self, bad_guess):
        """
        affiche le pendu en fonction du nombre de fausses lettres.
        """
        self.print_ascii(f"ressources/pendus11/pendu{len(bad_guess)}.txt")
            
    def bravo_normal(self):
        """
        affiche l'ecran de victoire.
        """   
        self.print_ascii("ressources/end_screen/win.txt")
        
    def loose_normal(self):
        """
        affiche l'ecran de fin quand le joueur perd.
        """
        self._init_end_screen()
        self.print_ascii("ressources/end_screen/lose.txt")
        
        print(f"\nLe mot etait : {''.join(self.word_list)}")
        input("\nAppuyez sur entrer pour continuer...")