import string

print("\n=== JOB 7 ===")
"""
Job 7
"""
class Character():
    def __init__(self, y, x, sign="X"):
        self.x = x
        self.y = y
        self.sign = sign

    def __str__(self):
        return f"la position actuelle du personnage est : {self.position()}"
    
    def move_up(self, board):
        board.clear_previous_emplacement(self.x, self.y)
        if self.y > 1:
            self.y -= 1
            board.update_board(self)
        else: 
            print("\n vous ne pouvez pas monter plus haut")
        
    def move_down(self, board):
        board.clear_previous_emplacement(self.x, self.y)
        if self.y < len(board.board)-1:
            self.y += 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas descendre plus bas")
        
    def move_left(self, board):
        board.clear_previous_emplacement(self.x, self.y)
        if self.x > 1:
            self.x -= 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas aller sur la gauche")
        
    def move_right(self, board):
        board.clear_previous_emplacement(self.x, self.y)
        if self.x < len(board.board[0])-1:
            self.x += 1
            board.update_board(self)
        else:
            print("\n vous ne pouvez pas vous déplacer sur la droite")
    
    def position(self):
        return (self.x, self.y)
    
class Board():
    alphabet = string.ascii_uppercase

    def __init__(self, rows, columns):
        self.rows = rows +1
        self.columns = columns +1
        self.board = self.create_board()
    
    def clear_previous_emplacement(self, x, y):
        self.board[y][x] = " "

    def create_board(self):
        board = []
        row_list = []
        for index in range(self.rows):
            row_list = []
            for other_index in range(self.columns):
                if index == 0 and other_index == 0:
                    content = "  "
                    row_list.append(content)
                elif index == 0:
                    content = self.alphabet[other_index-1]
                    row_list.append(content)
                elif other_index == 0:
                    if index < 10:
                        content = f"{index} "
                    else:
                        content = index
                    row_list.append(content)
                else:
                    content = " "
                    row_list.append(content)
            board.append(row_list)
        return board

    def display_board(self):
        print("\n")
        for i in range(self.rows):
            for j in range(self.columns):
                box = f"{self.board[i][j]} | "
                print(box, end="")
            print("")
            line = "---+"
            for index in range(self.columns-1):
                line += "---+"
            print(line)

    def update_board(self, character):
        self.board[character.y][character.x] = character.sign
        self.display_board()
            
board = Board(5,5)
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