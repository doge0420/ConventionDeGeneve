class PLAYER:
    def __init__(self, name, pseudo) -> None:
        self.name = name
        self.pseudo = pseudo
        self.score = 0

    def add_score(self, score):
        """
        additione le total des scores et le nouveau
        """
        self.score += score

    def sub_score(self, score):
        """
        soustrait le total des scores et le nouveau
        """
        self.score -= score