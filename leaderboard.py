import json

class LEADERBOARD:
    def __init__(self):
        with open(f"ressources/leaderboard.json", "r") as f:
            self.board = json.load(f)

    def _dump_json(self):
        """
        sauvegarde le leaderboard sur leaderboard.json
        """
        with open(f"ressources/leaderboard.json", "w") as f:
            json.dump(self.board, f, indent=4)

    def add_scoreboard(self, score, name):
        """
        vérifie si le nom de l'utilisateur est déja inscrit dans le scoreboard, 
        si oui il le compare à l'ancien score de l'utilisateur
        si le nouveau score est meilleur que le nouveau,l'ancien score est remplacé par le nouveau. 
        sinon, rien n'a lieu
        """
        if name in self.board.keys():
            if self.board[name] < score:
                self.board[name] = score
                self._dump_json()
            else:
                print("\nVous avez déjà un meilleur score dans le leaderboard\n")
        else:
            self.board[name] = score
            self._dump_json()

    def show_scoreboard(self):
        """
        trie le leaderboard par score et l'affiche dans le terminal
        """
        dict_sort = dict(sorted(self.board.items(), key=lambda x : -x[1]))

        for i, name in enumerate(dict_sort.keys()):
            print(f"{i+1}. {name} - {dict_sort[name]} pts")

if __name__ == "__main__":
    #test
    name = "ndava" 
    score = 999999999999
    lead = LEADERBOARD()
    # lead.add_scoreboard(score, name)
    lead.show_scoreboard()