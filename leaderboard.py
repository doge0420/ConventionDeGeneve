import player

class LEADERBOARD:
    def __init__(self,name,score):
        board = score
        score = {}
        
    
    def add_scoreboard(self,score,name,board):
        board[name] = score

    def show_scoreboard(self,board,name):
        scorelist = []
        for x in board.keys():
            scorelist.append(x)

        scorelist.sort()
        n = 1
        for y in scorelist:
            print("{0}. {1}".format(n, board[y]))
            n +=1


#test
name = "lol" 
score = 12
swag = LEADERBOARD(name,score)
swag.add_scoreboard
print(swag.show_scoreboard)

        