from Piece import *
from RedPiece import *
from BlackPiece import *

class Board:
    
    def __init__(self):
        self.player = "R"
        
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
        for height in range(8):
            print(height, end=' ')
            for width in range(8):
                if self.board[height][width] == None:
                    print("[ ]", end='')
                else:
                    print(f"{self.board[height][width].display()}", end='')
            print()
            
            
    def is_legal_move(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        return (piece != None and piece.get_color() == self.player 
                and self.board[new_y][new_x] == None 
                and piece.is_valid_move(new_x, new_y))
    
    def player_move(self, x, y, new_x, new_y):
        piece = self.board[y][x]
        if self.is_legal_move(x, y, new_x, new_y):
            self.board[new_y][new_x] = self.board[y][x]
            self.board[y][x] = None
            piece.move(new_x, new_y)
            return True
        return False
    
    
    def change_player(self, x, y, new_x, new_y):
        if (self.player_move(x, y, new_x, new_y) or 
            self.player_jump(x, y, new_x, new_y)):
            if self.player == "R":
                self.player = "B"
            else:
                self.player = "R"
        return self.player
    
    
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
            return True
        return False
    
    def check_king(self, x, y, new_x, new_y):
        if (self.player_move(x, y, new_x, new_y) or 
            self.player_jump(x, y, new_x, new_y)):
        if new_y == 7 or new_y == 0:
            self.king_piece(new_y)
    
    
    def king_piece(self, y):
        piece = self.board[y][x]
        if piece.get_color() == self.player:
            if y == 7 and piece.get_color == 'R':
                self.board[y][x] == piece.king()
            elif y == 0 and piece.get_color == 'B':
                self.board[y][x] == piece.king()
 
 
 
#===============================================================================               
if __name__ == "__main__":                            
    board = Board()
    board.display()
    #print(board.is_legal_move(0, 0, 1, 1))
    
    #print(board.player_move(2, 2, 1, 3))
    print(board.change_player(2, 2, 3, 3))
    board.display()

    print(board.change_player(1, 5, 2, 4))    
    board.display()
    
    print()
    board.player_jump(3, 3, 1, 5)
    board.display()