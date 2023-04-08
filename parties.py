from gui import GUI
from random import choice

class PARTIES:
    def __init__(self, gui):
        self.gui = gui # attend que le joueur choisisse play
        
        self.least_used_letters = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']
    
    def choose_word(self):
        with open("words.txt", "r") as f:
            words = f.readlines()
            
        return choice(words).strip()
        
    def word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.least_used_letters:
                bonus += 2

        return lenght + bonus
        
if __name__ == "__main__":
    PARTIES(GUI())