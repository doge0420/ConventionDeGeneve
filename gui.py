class GUI:

    def __init__(self):
        with open("title.txt", "r", encoding="utf-8") as f:
            print(f.read() + "\n1. PLAY \n2. GAME MODE \n3. HOW TO PLAY")
        
ok = GUI()


    