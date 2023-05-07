import json
from random import choice

class WORD:
    def get_word(self, difficulte):
        """
        prend la difficulté du mot en tant qu'argument et retourne un mot de words.json.
        """
        with open("ressources/data/words.json", "r") as f:
            words = json.load(f)

        word_range = words[difficulte]
        word_choice = choice(list(word_range.items()))

        self.word_list = [i for i in word_choice[0]]

        return self.word_list, word_choice[1]
    
    def check_win(self, guesses):
        """
        vérifie si toutes les lettres dans word_list (lettres à deviner) 
        sont contenues dans guesses (lettres devinées)
        si oui, la fonction retourne True, sinon False
        """
        return all(i in guesses for i in self.word_list)
    
    # plus besoin
    def word_difficulty(self, word):
        """
        calcule la difficulté du mot.
        difficulté = longueur du mot + le nombre de lettres peu communes dedans
        """
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.LEAST_USED_LETTERS:
                bonus += 2

        return lenght + bonus

    