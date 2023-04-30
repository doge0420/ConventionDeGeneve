import json

class LEADERBOARD:
    def __init__(self):
        with open("ressources/leaderboard.txt", "r") as f:
            self.board = json.load(f)
            
    def __del__(self):
        json.dump(self.board, open("ressources/leaderboard.txt", "w"))
            
    def add_scoreboard(self, score, name):
        if name in self.board.keys():
            if self.board[name] < score:
                self.board[name] = score
            else:
                print("Vous avez déjà un meilleur score")
        else:
            self.board[name] = score

    def show_scoreboard(self, name):
        scorelist = []
        for x in self.board.keys():
            scorelist.append(x)

        scorelist.sort()
        
        for i, y in enumerate(scorelist):
            print(f"{i}. {self.board[y]}")
           

#test
name = "lol" 
score = 12
swag = LEADERBOARD(name,score)
swag.add_scoreboard()
swag.show_scoreboard()