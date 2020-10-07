'''*****************************************************************************
Jason Lee
Wed, Oct 02, 2020
Checkers

This library contains all the info needed to king a black checkers piece for 
the textbased checkers game. BlackKing inherits from BlackPiece, and overwrites
the display of the piece to represent it is a king, as well as the 
is_valid_move and is_valid_jump methods to allow for forward and backward 
movement.

It also contains tests for the class as well.

*****************************************************************************'''

from BlackPiece import *

class BlackKing(BlackPiece):
    
    def display(self):
        '''
        Method used to display the BlackKing object on the board object in
        Board.py.
        
        Parameters:
                   -- self
        Returns:
                  -- "[B]", displayed on the board object
        '''        
        return "[B]"


    def is_valid_move(self, new_x, new_y):
        '''
        Method used to check if the move is valid. Returns True or False
        based on if the coordinates are one space to the left or right
        and one space up or down from the current coordinates.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- True or False, depending on if conditions are met.
        '''        
        return (self.y + 1 == new_y or self.y - 1 == new_y) and (
            self.x + 1 == new_x or self.x - 1 == new_x)
    
    
    def is_valid_jump(self, new_x, new_y):
        '''
        Method used to check if the jump is valid. Returns True or False
        based on if the coordinates are two spaces to the left or right
        and two spaces up or down from the current coordinates.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- True or False, depending on if conditions are met.
        '''        
        return (self.y + 2 == new_y or self.y - 2 == new_y) and (
            self.x + 2 == new_x or self.x - 2 == new_x)
    
    
#===============================================================================
if __name__ == "__main__":
    piece = BlackKing(4, 4)
    print((piece.x, piece.y), piece.get_color())
    
    for row in range(3, 6):
        for col in range(3,6):
            print(f"Move from (4, 4) to ({row}, {col})?", 
                  piece.is_valid_move(row, col))   