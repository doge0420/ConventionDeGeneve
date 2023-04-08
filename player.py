class PLAYER:
    def __init__(self, name, pseudo) -> None:
        self.name = name
        self.pseudo = pseudo
        self.score = 0

    def add_score(self, score):
        self.score += score

    def sub_score(self, score):
        self.score -= score