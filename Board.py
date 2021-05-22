'''*****************************************************************************
Jason Lee
Wed, Oct 02, 2020
Checkers

This library contains all the info needed to create a Board object for 
the textbased checkers game. The Board class contains an constructor, which
creates a 2D array for the board, and initiates the player by random. 
The class contains the methods:

-- display, which displays the board and pieces when called
-- change_player, which will change the player after their move has finished.
-- move, which checks a players input for a move (either a jump or move)
-- player_jump, which executes a jump for the current player
-- player_move, which executes a move for the current player
-- is_legal_move, which determines if the players input is a legal move based on
   checkers rules.
-- is_legal_jump, which determines if the players input is a legal jumpbased on
   checkers rules.
-- check_jump, which determines if the player can make another jump before their
   turn is over.
-- check_king, which checks if a player's piece has reached the end of the board
   for that piece's direction
-- king_piece, which kings the player's piece.
-- game_end, which ends the game if one player has no pieces left.


*****************************************************************************'''

from Piece import *
from RedPiece import *
from BlackPiece import *
from BlackKing import *
from RedKing import *
from copy import deepcopy
import random


class Board:

    black_pieces = 12
    red_pieces = 12
    black_kings = 0
    red_kings = 0
    
    def __init__(self):
        #the player to start is always Black
        self.player = "Black"
        
        #board is made of a list of lists (2D array)
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
        '''
        Method used to display the board, using A - H for col 
        selection (or x), and 1 - 8 as row selection (or y).
        '''
        #each x coordinate represented by a letter (each column)
        print("   A  B  C  D  E  F  G  H")
        for height in range(8):
            #y coordinate represented by a number (each row)
            print(f"{height + 1} ", end='')
            for width in range(8):
                if self.board[height][width] == None:
                    print("[ ]", end='')
                else:
                    print(f"{self.board[height][width].display()}", end='')
            print(f" {height + 1}")
        print("   A  B  C  D  E  F  G  H")
        
    
    def change_player(self):
        '''
        Method used to change the player (red or black), by checking who the
        current player is. Either "Red" or "Black".
        
        Returns:
                  -- self.player, the new current player. 
        '''        
        if self.player == "Red":
            self.player = "Black"
        else:
            self.player = "Red"
        return self.player    
    
    def move(self, x, y, new_x, new_y):
        '''
        Method used to interpret the player's input for their turn. 
        Takes player input as an argument. It checks to see if the input is a 
        valid jump or valid move, in which case it will execute a jump or move, 
        or prints an error saying the move is not possible. If a jump is possible
        anywhere on the board, the method will print a statement saying so.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
                   -- new_x, new requested x coordinate for selected piece
                   -- new_y, new requested y coordinate for selected piece
        Returns:
                  -- self.player, the new current player. 
        '''
        
        if self.is_legal_jump(x, y, new_x, new_y):
            self.player_jump(x, y, new_x, new_y)
            return

        true_move = self.is_legal_move(x, y, new_x, new_y)
        if true_move == True:
            if not (self.player_move(x, y, new_x, new_y)):
                print(f"Player {self.player} must jump.")  
            return
        elif true_move == False:
            print("Move is not possible.\n")
            return 
        else:
            print(f"{self.player} player must jump.")
            return 
        
    
    def is_legal_move(self, x, y, new_x, new_y):
        '''
        Method used to check the player's input for a valid move. Returns
        True or False depending on whether the move is valid or not. Checks
        if the current coordinates contain a piece, if that piece
        corresponds to the player's piece color, if the new coordinates are 
        empty, and then if the piece itself has a valid move.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
                   -- new_x, new requested x coordinate for selected piece
                   -- new_y, new requested y coordinate for selected piece
        Returns:
                  -- True or False, if the move is valid or not.
        '''
        piece = self.board[y][x]
        if not self.check_jump_all(): 
            return (piece != None 
                    and piece.get_color() == self.player 
                    and (new_x >= 0 and new_x <= 7)
                    and (new_y >= 0 and new_y <= 7)
                    and self.board[new_y][new_x] == None 
                    and piece.is_valid_move(new_x, new_y))
        else:
            return 
    
    
    def is_legal_jump(self, x, y, new_x, new_y):
        '''
        Method used to check the player's input for a valid jump. Returns
        True or False depending on whether the jump is valid or not. Checks
        if the current coordinates contain a piece, if that piece
        corresponds to the player's piece color, if the new coordinates are 
        empty, and then if the piece itself has a valid jump.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
                   -- new_x, new requested x coordinate for selected piece
                   -- new_y, new requested y coordinate for selected piece
        Returns:
                  -- True or False, if the jump is valid or not.
        '''
        try:
            piece = self.board[y][x]
            enemy_piece = self.board[(y + new_y) //2][(x + new_x) // 2]
            return (piece != None and piece.get_color() == self.player
                    and enemy_piece != None 
                    and enemy_piece.get_color() != self.player
                    and self.board[new_y][new_x] == None
                    and (new_x >= 0 and new_x <= 7)
                    and (new_y >= 0 and new_y <= 7)
                    and piece.is_valid_jump(new_x, new_y))
        except IndexError:
            return False
    
    
    def player_move(self, x, y, new_x, new_y):
        '''
        Method used to execute the player's input for the move. initiates a 
        piece on the board in the provided coordinates, and checks if the move
        is legal, and makes sure a jump is not possible (as per checker rules)
        and then executes the move by setting the new coordinates equal to the
        piece, and then removing the piece from the old coordinates. Then the 
        function checks for a king, and then changes the player.
        
        If a jump is possible, player must jump, and a error message is 
        displayed saying this.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
                   -- new_x, new requested x coordinate for selected piece
                   -- new_y, new requested y coordinate for selected piece
        Returns:
                  -- None
        '''           
        piece = self.board[y][x]
        if (self.is_legal_move(x, y, new_x, new_y) and 
            not self.check_jump_current(x, y)):
            self.board[new_y][new_x] = self.board[y][x]
            self.board[y][x] = None
            piece.move(new_x, new_y)
            self.check_king(new_x, new_y)
            self.change_player()
            return True
        else:
            return False 
    
    
    def player_jump(self, x, y, new_x, new_y):
        '''
        Method used to execute the player's input for the move. Initiates a 
        piece on the board in the provided coordinates, and checks if the jump
        is legal, then executes the move by setting the new coordinates equal to 
        the piece, and then removing the piece from the old coordinates. Then 
        the function checks for a king, and then checks for another possible 
        jump. If the another jump is possible, the player continues, else
        the player will be changed.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
                   -- new_x, new requested x coordinate for selected piece
                   -- new_y, new requested y coordinate for selected piece
        Returns:
                  -- None
        '''        
        piece = self.board[y][x]        
        if self.is_legal_jump(x, y, new_x, new_y):
            self.board[new_y][new_x] = self.board[y][x]
            self.board[y][x] = None
            self.board[(y + new_y) // 2][(x + new_x) // 2] = None
            piece.jump(new_x, new_y)
            self.check_king(new_x, new_y)

            # decrements the pieces on the board
            if self.player == "Black":
                self.red_pieces -= 1
            else:
                self.black_pieces -= 1
            
            if not self.check_jump_current(new_x, new_y):
                self.change_player()
            return True
        return False
        
        
    def check_jump_current(self, x, y):
        '''
        Method used to check if another jump is possible for the current piece
        in question. The argument is the new coordinates for the piece. The
        method checks if a jump is valid in any direction (for both pieces
        and kings), and if it returns True, the player continues their turn.
        
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
        Returns:
                  -- True or False, if jump is possible or not.
        '''
        return (self.is_legal_jump(x, y, x - 2, y - 2) 
        or self.is_legal_jump(x, y, x + 2, y - 2) 
        or self.is_legal_jump(x, y, x - 2, y + 2) 
        or self.is_legal_jump(x, y, x + 2, y + 2))
        
    def check_jump_all(self):
        '''
        Method used to check if a jump is possible for the current player. The
        method iterates through the board, and if any of the pieces can jump,
        the method returns True. Else returns False
                
        Parameters:
                   -- self
        Returns:
                  -- True or False, if jump is possible or not.
        '''         
        for row in range(8):
            for col in range(8):
                if (self.board[row][col] != None 
                    and self.board[row][col].get_color() == self.player
                    and self.check_jump_current(col, row)):
                    return True
        return False
        
    def choose_move_easy(self):
        '''
        Method used to choose a move from a list of moves for the computer
        player. calls the move_list function to build a dictionary of moves
        with the current piece as the key and it's moves as the items. It
        then chooses a move from the dictionary by random choice.

        Returns:
                    -- move, randomly selected move for a piece.
        '''
        move = []
        moves = self.move_list()
        move = random.choice(list(moves.items()))
        # if a piece is selected that doesn't have any moves, then select 
        # another piece
        while move[1] == []:
            move = random.choice(list(moves.items()))
        return move
        
    def choose_move_hard(self):
        '''
        Method used to get a move from the minimax method. Decides if 
        the player calling the method is the minimizing or maximizing player
        '''
        if self.player == "Red":
            return self.mini_max(3, False)[1]
        else:
            return self.mini_max(3, True)[1]
        


    def mini_max(self, depth, max_p):
        '''
        Minimax - recursive algorithm used to calculate the best possible
        path to be taken by the computer. It recursively calls until the depth 
        is 0 or the game is ended, and each node visited is assigned a score 
        based on the current number of black pieces - red pieces. If the player
        is the max player, then the algorithm chooses the max score from all 
        nodes visited at that level. if the player is the min player, the 
        algorithm will choose the lowest score for that level. 
        '''
        if depth == 0:
            return self.eval_move(), self.board
        elif self.game_end():
            return self.eval_move(), self.board
        b_list = []
        b_list = self.board_list()
        if max_p:
            max_score = -100000.00
            best = None
            for b, p, m in b_list:
                score = b.mini_max(depth - 1, False)[0]
                max_score = max(max_score, score)
                if max_score == score:
                    best = [p, m]
            return max_score, best
        else:
            min_score = 100000.00
            best = None
            for b, p, m in b_list:
                score = b.mini_max(depth - 1, True)[0]
                min_score = min(min_score, score)
                if min_score == score:
                    best = [p, m]
            return min_score, best


    def board_list(self):
        '''
        Method used to build a list of board objects to represent each possible
        move the AI could take in order to allow the minimax algorithm to choose
        the best score for minimizing or maximizing player.
        '''
        b_list = []

        m_list = self.move_list()
        for piece in m_list:
            for move in m_list[piece]:
                new_board = deepcopy(self)
                (x, y) = piece
                (new_x, new_y) = move
                if new_board.player_move(x, y, new_x, new_y):
                    b_list.append([new_board, piece, move])
                elif new_board.player_jump(x, y, new_x, new_y):
                    b_list.append([new_board, piece, move])
        return b_list


    def eval_move(board):
        '''
        Simple method used to return the difference between the remaining red
        and black pieces on the board. Also adds the difference between the 
        black kings and red kings, which are each multiplied by 5. This 
        is to incentivize the AI to attempt to make kings instead of only going
        for jumps.
        '''
        return board.black_pieces - board.red_pieces + (board.black_kings * 0.5 - board.red_kings * 0.5)

 
    def move_list(self):
        '''
        Method used to build dictionary containing moves for all the computer's
        pieces. This method iterates through the board and finds all the pieces
        that belong to the computer. The method calls the check_moves method
        to find all the moves that each piece can make on the board. This method
        returns the moves list. 

        Returns:
                    -- moves, a dictionary containing moves for the computer's 
                       pieces
        '''
        moves = {}
        for row in range(8):
            for col in range(8):
                if (self.board[row][col] != None 
                and self.board[row][col].get_color() == self.player):
                    moves[(col, row)] = []
                    moves = self.check_moves(col, row, moves)
        return moves

    def check_moves(self, x, y, moves):
        '''
        Method used to check moves for the current piece in question when called
        by the move_list method. This method checks if the move is legal, and
        if it returns false, the player must jump, and so the piece is checked
        for a legal jump.

        Parameters:
                    - x, the x coordinate for the piece in question
                    - y, the y coordinate for the piece in question
                    - moves, a dictionary to add moves that are found for the 
                      piece in question.
        Returns:
                    - moves, a dictionary containing all found moves for the
                      piece in question.
        '''
        try:
            # each is_legal_move will return False if the current piece 
            # must jump. So if one returns false, they all will, leading to
            # possible jumps being searched for instead of moves. 
            if self.is_legal_move(x, y, x + 1, y + 1):
                moves[(x, y)].append((x + 1, y + 1))
            elif self.is_legal_jump(x, y, x + 2, y + 2):
                moves[(x, y)].append((x + 2, y + 2))

            if self.is_legal_move(x, y, x + 1, y - 1):
                moves[(x, y)].append((x + 1, y - 1))
            elif self.is_legal_jump(x, y, x + 2, y - 2):
                moves[(x, y)].append((x + 2, y - 2))

            if self.is_legal_move(x, y, x - 1, y + 1):
                moves[(x, y)].append((x - 1, y + 1))
            elif self.is_legal_jump(x, y, x - 2, y + 2):
                moves[(x, y)].append((x - 2, y + 2))

            if self.is_legal_move(x, y, x - 1, y - 1):
                moves[(x, y)].append((x - 1, y - 1))
            elif self.is_legal_jump(x, y, x - 2, y - 2):
                moves[(x, y)].append((x - 2, y - 2))
        except IndexError:
            pass

        return moves
            

    def check_king(self, x, y):
        '''
        Method used to check if the piece in question can be kinged. The 
        argument is the new coordinates for the piece. The method checks if
        the current piece is at the enemies end of the board, and if it is, 
        calls the king_piece method.
        
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
        Returns:
                  -- None
        '''          
        if y == 7 or y == 0:
            self.king_piece(x, y)
    
    
    def king_piece(self, x, y):
        '''
        Method used to king the piece in question. The argument is the new 
        coordinates for the piece. The method checks if the current piece 
        corresponds to the players color, and if it is at the enemies end of the
        board, and if it is, it calls creates a King object (Red or Black 
        depending on color of piece), and replaces the current piece with the
        King piece.
        
        Parameters:
                   -- x, current x coordinate of selected piece
                   -- y, current y coordinate of selected piece
        Returns:
                  -- None
        '''         
        piece = self.board[y][x]
        if piece.get_color() == self.player:
            if (y == 7 and piece.get_color() == "Red"):
                self.board[y][x] = RedKing(x, y)
                self.red_kings += 1
            elif (y == 0 and piece.get_color() == "Black"):
                self.board[y][x] = BlackKing(x, y)
                self.black_kings += 1
    
    def game_end(self):
        '''
        Method used to check if the game has ended. The method iterates through
        the list of lists in the board, and checks if there are pieces remaining
        for each color. If one player doesn't have any remaining pieces, the 
        game is over and the other player has won.
        
        Parameters:
                   -- self
        Returns:
                  -- True or False, depending on if no pieces remain for one
                  of the players.
        '''
        if self.red_pieces == 0:
            self.display()
            print("Black Wins!")
            return True
        elif self.black_pieces == 0:
            self.display()
            print("Red Wins!")
            return True
        else:
            return False
                
    

 
 
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
    