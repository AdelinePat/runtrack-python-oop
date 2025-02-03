print("\n=== JOB 7 ===")
"""
Job 7
"""
class Character():
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.sign = "X"

    def move_up(self, board):
        self.clear_previous_emplacement(board)
        if self.y > 1:
            self.y -= 1
        else: 
            print("vous ne pouvez pas monter plus haut")
        self.update_board(board)
    
    def move_down(self, board):
        self.clear_previous_emplacement(board)
        if self.y < len(board)-1:
            self.y += 1
        else:
            print("vous ne pouvez pas descendre plus bas")
        self.update_board(board)
    
    def move_left(self, board):
        self.clear_previous_emplacement(board)
        if self.x > 1:
            self.x -= 1
        else:
            print("vous ne pouvez pas aller sur la gauche")
        self.update_board(board)
    
    def move_right(self, board):
        self.clear_previous_emplacement(board)
        if self.x < len(board[0])-1:
            self.x += 1
        else:
            print("vous ne pouvez pas vous déplacer sur la droite")
        self.update_board(board)
    
    def clear_previous_emplacement(self, board):
        board[self.y][self.x] = " "
    
    def update_board(self, board):
        board[self.y][self.x] = self.sign
        display_board(board)

    def position(self):
        return (self.x, self.y)

def display_board(board):
    print("\n")
    for i in range(len(board)):
        for j in range(len(board)):
            box = f"{board[i][j]} | "
            print(box, end="")
        print("")
        line = "--+"
        for index in range(len(board)-1):
            line += "---+"
        print(line)

little_one = Character(2, 1)
# board = [["", "", ""],["", "", ""],["", "", ""]]
board =  [[" ", "A", "B", "C", "D"], [1," "," "," ", " "], [2," "," "," ", " "], [3," "," ", " ", " "], [4," "," ", " ", " "]]
board[little_one.y][little_one.x] = little_one.sign
display_board(board)

little_one.move_down(board)
little_one.move_down(board)
little_one.move_right(board)
# display_board(board)
# little_one.update_board(board)

little_one.move_left(board)
little_one.move_left(board)
little_one.move_right(board)
# little_one.update_board(board)

little_one.move_right(board)
little_one.move_up(board)

# little_one.update_board(board)
print(f"la position actuelle du personnage est : {little_one.position()}")
