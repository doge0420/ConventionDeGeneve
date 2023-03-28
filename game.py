class jeu:
    def __init__(self):
        self.least_used_letters = ['w', 'k', 'x', 'y', 'z', 'j', 'q', 'v', 'f', 'h']

    def word_difficulty(self, word):
        lenght = len(word)

        bonus = 0
        for letter in word:
            if letter in self.least_used_letters:
                bonus += 2

        return lenght + bonus

    def 

if __name__ == "__main__":
    game = jeu()