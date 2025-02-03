import string

print("\n=== JOB 7 ===")
"""
Job 7
"""
class Character():
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.sign = "X"

    def __str__(self):
        return f"la position actuelle du personnage est : {little_one.position()}"
    
    def move_up(self, board):
        self.clear_previous_emplacement(board)
        if self.y > 1:
            self.y -= 1
            board.update_board(self)
        else: 
            print("\n vous ne pouvez pas monter plus haut")
        
    def move_down(self, board):
        self.clear_previous_emplacement(board)
        if self.y < len(board.board)-1:
            self.y += 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas descendre plus bas")
        
    def move_left(self, board):
        self.clear_previous_emplacement(board)
        if self.x > 1:
            self.x -= 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas aller sur la gauche")
        
    def move_right(self, board):
        self.clear_previous_emplacement(board)
        if self.x < len(board.board[0])-1:
            self.x += 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas vous déplacer sur la droite")
         
    def clear_previous_emplacement(self, board):
        board.board[self.y][self.x] = " "
    
    def position(self):
        return (self.x, self.y)
    
class Board():
    alphabet = string.ascii_uppercase

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = self.create_board()

    def create_board(self):
        board = []
        row_list = []
        for index in range(self.rows):
            row_list = []
            for other_index in range(self.columns):
                if index == 0 and other_index == 0:
                    content = " "
                    row_list.append(content)
                elif index == 0:
                    content = self.alphabet[other_index-1]
                    row_list.append(content)
                elif other_index == 0:
                    content = index
                    row_list.append(content)
                else:
                    content = " "
                    row_list.append(content)
            board.append(row_list)
        return board


    def display_board(self):
        print("\n")
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                box = f"{self.board[i][j]} | "
                print(box, end="")
            print("")
            line = "--+"
            for index in range(len(self.board)-1):
                line += "---+"
            print(line)

    def update_board(self, character):
        self.board[character.y][character.x] = character.sign
        self.display_board()
            
board = Board(6,6)
little_one = Character(3,2)
board.board[little_one.y][little_one.x] = little_one.sign

board.display_board()

little_one.move_down(board)
little_one.move_down(board)
little_one.move_right(board)
print(little_one)
little_one.move_left(board)
little_one.move_left(board)
little_one.move_right(board)

little_one.move_right(board)
little_one.move_up(board)
print(little_one)
