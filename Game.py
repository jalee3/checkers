'''=============================================================================
REF's
-- https://www.siammandalay.com/blogs/puzzles/checkers-game-basic-rules-win
(rules for the checkers game)
============================================================================='''

from pprint import pprint
from Board import *

def game():
    print("-----Checkers-----\n")
    rules()
 
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
    if (len(user_input) == 2 
        and int(user_input[1]) in range(1, 9) 
        and user_input[0].lower() in "abcdefgh"):
            x = "abcdefgh".index(user_input[0].lower())
            y = int(user_input[1]) - 1
            return x, y


def rules():
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
game()