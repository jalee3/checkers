'''*****************************************************************************
Jason Lee
Wed, Oct 02, 2020
Checkers

This program is a text-based classic checkers game. The game allows two players 
to make moves, trying to remove each others pieces off the board until one 
player has no remaining pieces left. When this occurs, the other player has won 
the game. The player that starts is chosen randomly. 


Rules:
    -- A player's turn is defined as either moving a piece, or jumping an enemy
    piece.
    -- the pieces must move diagonally forwards to the enemies side of the
    board, not backwards (King pieces being the exception). Players can only
    move one piece per turn.
    --a jump can occur if a enemy piece is one space away from the players piece
    and the space behind that piece is empty (where a space is one step 
    diagonally forward).
    -- If a jump is possible, the player must jump (If multiple jumps available
    the player can choose between them).
    --
    -- If a player's piece reaches the end of the enemies side of the board, 
    that piece is kinged, and can now move either forward or backward.
    -- Once one player has removed all the enemy pieces, that player has won.
    

This program uses the Board.py library, which calls the other libraries 
(Piece.py, RedPiece.py, BlackPiece.Py, BlackKing.py, RedKing.py) in order to 
implement all the methods required for Board.py to execute the game. 

REF's
-- https://www.siammandalay.com/blogs/puzzles/checkers-game-basic-rules-win
(rules for the checkers game)

*****************************************************************************'''
import time
from Board import *

def main():
    '''
    This function runs the game. It prints the name of the game, the legend,
    calls the rule print function, and then initiates the board object from 
    Board.py library. The function loops through each players turn until
    the game has ended, which is the game_end() method for the board class which
    checks to see if one of the players has no remaining pieces. Once one player
    has no remaining pieces, the game has ended and the program ends. 
    '''    
    print("\n-----Checkers-----\n")
    rules()
    time.sleep(5) 
    
    print("Legend:")
    print("r - red piece\t R - red king")
    print("b - black piece\t B - black king\n")    
    
    board = Board()
    while not board.game_end():
        
        player = board.player
        if player == "R":
            player = "Red"
        else:
            player = "Black"
            
        print(f"{player}'s turn!") 
        time.sleep(1)
        print()
        board.display()
        print()
        
        piece = input(f"{player} player, choose your piece: ")
        x, y = check_input(piece)
        
        move = input(f"{player} player, choose your move: ")
        new_x, new_y = check_input(move)
        print()
        
        board.move(x, y, new_x, new_y)
        
        
                
def check_input(user_input):
    '''
    Function used to check the users input to determine if it is a valid
    coordinate as defined by the board layout, and returns the value 
    as integers to be used in the Board.py library to move the specified piece
    to the specified coordinates.
    
    Parameters:
               -- user_input, the users input for coordinates.
    Returns:
              -- x, the x coordinate of the users input
              -- y, the y coordinate of the users input
    '''       
    if (len(user_input) == 2 
        and int(user_input[1]) in range(1, 9) 
        and user_input[0].lower() in "abcdefgh"):
            x = "abcdefgh".index(user_input[0].lower())
            y = int(user_input[1]) - 1
            return x, y


def rules():
    '''
    Function used to display the rules of checkers, as defined on the website:
    
    https://www.siammandalay.com/blogs/puzzles/checkers-game-basic-rules-win
    (rules for the checkers game)
    '''       
    print("Rules:")
    print("1. The two players alternate turns and can only move their own pieces.")
    print("2. Each turn involves the moving of one piece, which can consist of a"
          " piece moving forward to a diagonally adjacent square that is"
          " unoccupied,\n   or jumping forward over an occupied diagonally adjacent" 
          " square, provided that the square beyond is also empty.")
    print("3. If a player jumps over their opponent's piece, they have successfully"
          "captured that piece and it is removed from the game.")
    print("4. Each piece is initially referred to as a man, but if it reaches the" 
          " furthest side of the board it becomes a king.\n   When this happens, the"
          " player stacks an additional piece on top of the original to signify" 
          " the change.")
    print("5. Men may only move forward, but kings can move diagonally forwards as"
          " well as backwards.")
    print("6. Multiple pieces maybe jumped by both men and kings provided that"
          " there are successive unoccupied squares beyond each piece that is" 
          " jumped.\n")
    
main()