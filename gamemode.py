from PIL import Image

class GAMEMODE():
    def ___init___(self):
        if self.choice["mode_incredible"] == True:
            return self._mode_incredible
        else:
            return self._mode_normal

    def _mode_incredible(self, win=False):
        if win:
            with Image.open("ressources/incredible/mincredible_bravo.png") as f:
                f.show()
        else:
            with Image.open(f"ressources/incredible/mincredible{len(self.bad_guess)}.png") as f:
                f.show()

    def _mode_normal(self):
        print("\n\n")
        with open (f"ressources/pendus11/pendu{len(self.bad_guess)}.txt", "r", encoding="utf-8") as f:
            print(f.read())