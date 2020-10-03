from Piece import *
from RedPiece import *
from BlackPiece import *
from BlackKing import *
from RedKing import *
import random


class Board:
    
    def __init__(self):
        self.player = random.choice(["R", "B"])
        
        self.board = []
        for height in range(8):
            line = []
            for width in range(8):
                if (height + width) % 2 == 0:
                    if height <= 2:
                        line.append(RedPiece(width, height))
                    elif height >= 5:
                        line.append(BlackPiece(width, height))
                    else:
                        line.append(None)
                else:
                    line.append(None)
            self.board.append(line)
    
    
    def display(self):
        print("   A  B  C  D  E  F  G  H")
        for height in range(8):
            print(f"{height + 1} ", end='')
            for width in range(8):
                if self.board[height][width] == None:
                    print("[ ]", end='')
                else:
                    print(f"{self.board[height][width].display()}", end='')
            print(f" {height + 1}")
        print("   A  B  C  D  E  F  G  H")
        
    
    def change_player(self):
        if self.player == "R":
            self.player = "B"
        else:
            self.player = "R"
        return self.player    
    
    def move(self, x, y, new_x, new_y):
        if self.is_legal_jump(x, y, new_x, new_y):
            self.player_jump(x, y, new_x, new_y)
        elif self.is_legal_move(x, y, new_x, new_y):
            self.player_move(x, y, new_x, new_y)
        else:
            print("Move is not possible.\n")
            return    
    
    def is_legal_move(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        return (piece != None and piece.get_color() == self.player 
                and self.board[new_y][new_x] == None 
                and piece.is_valid_move(new_x, new_y))
    
    def player_move(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        if self.is_legal_move(x, y, new_x, new_y) and not self.check_jump(x, y):
            self.board[new_y][new_x] = self.board[y][x]
            self.board[y][x] = None
            piece.move(new_x, new_y)
            self.check_king(new_x, new_y)
            self.change_player()
        else:
            print(f"{self.player} player must jump.")
    
    
    def is_legal_jump(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        enemy_piece = self.board[(y + new_y) //2][(x + new_x) // 2]
        return (piece != None and piece.get_color() == self.player
                and enemy_piece != None 
                and enemy_piece.get_color() != self.player
                and self.board[new_y][new_x] == None
                and piece.is_valid_jump(new_x, new_y))
    
    
    def player_jump(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        enemy_piece = self.board[(y + new_y) //2][(x + new_x) // 2]        
        if self.is_legal_jump(x, y, new_x, new_y):
            self.board[new_y][new_x] = self.board[y][x]
            self.board[y][x] = None
            self.board[(y + new_y) // 2][(x + new_x) // 2] = None
            piece.jump(new_x, new_y)
            
            self.check_king(new_x, new_y)
            if not self.check_jump(new_x, new_y):
                self.change_player()
        
    def check_jump(self, x, y):
        if (x - 2 >= 0 and x + 2 <= 7) and (y - 2 >= 0 and y + 2 <= 7): 
            return (self.is_legal_jump(x, y, x + 2, y + 2) 
                    or self.is_legal_jump(x, y, x - 2, y + 2)
                    or self.is_legal_jump(x, y, x + 2, y - 2)
                    or self.is_legal_jump(x, y, x - 2, y - 2))
            

    def check_king(self, x, y):
        if y == 7 or y == 0:
            self.king_piece(x, y)
    
    
    def king_piece(self, x, y):
        piece = self.board[y][x]
        if piece.get_color() == self.player:
            if (y == 7 and piece.get_color() == "R"):
                self.board[y][x] = RedKing(x, y)
            elif (y == 0 and piece.get_color() == "B"):
                self.board[y][x] = BlackKing(x, y)
    
    def game_end(self):
        Black = False
        Red = False
        
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == "R":
                        Red = True
                    else:
                        Black = True
        if Black and Red:
            return False
        elif Red:
            print("Red Wins!")
            return True
        elif Black:
            print("Black Wins!")
            return True
                
    

 
 
#===============================================================================               
if __name__ == "__main__":                            
    board = Board()
    board.display()
    #print(board.is_legal_move(0, 0, 1, 1))
    
    #print(board.player_move(2, 2, 1, 3))
    print()
    board.player_move(2, 2, 3, 3)
    board.display()
    
    print()
    board.player_move(3, 3, 2, 4)    
    board.display()
       
    print()
    board.player_jump(2, 4, 3, 5)
    board.display()
    
    print()
    board.player_jump(3, 5, 2, 6)
    board.display()
    
    print()
    board.player_jump(2, 6, 3, 7)
    board.display()    
    