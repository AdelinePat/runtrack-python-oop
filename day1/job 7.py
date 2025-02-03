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
        if self.y > 0:
            self.y -= 1
        else: 
            print("vous ne pouvez pas monter plus haut")
    
    def move_down(self, board):
        self.clear_previous_emplacement(board)
        if self.y < len(board)-1:
            self.y += 1
        else:
            print("vous ne pouvez pas descendre plus bas")
    
    def move_left(self, board):
        self.clear_previous_emplacement(board)
        if self.x > 0:
            self.x -= 1
        else:
            print("vous ne pouvez pas aller sur la gauche")
    
    def move_right(self, board):
        self.clear_previous_emplacement(board)
        if self.x < len(board[0])-1:
            self.x += 1
        else:
            print("vous ne pouvez pas vous déplacer sur la droite")
    
    def clear_previous_emplacement(self, board):
        board[self.y][self.x] = ""
    
    def position(self):
        return (self.x, self.y)

little_one = Character(1, 0)
board = [["", "", ""],["", "", ""],["", "", ""]]
board[little_one.y][little_one.x] = little_one.sign
print(board)
little_one.move_down(board)
little_one.move_down(board)
little_one.move_right(board)
little_one.move_left(board)
little_one.move_left(board)
board[little_one.y][little_one.x] = little_one.sign
print(board)
print(little_one.position())
