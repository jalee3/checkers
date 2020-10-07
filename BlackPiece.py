'''*****************************************************************************
Jason Lee
Wed, Oct 02, 2020
Checkers

This library contains all the info needed to create a black checkers piece for 
the textbased checkers game. 
BlackPiece inherits from Piece, and overwrites the methods:
- display, to represent the black piece
- get_color, to return the color of the black piece
- is_valid_move, which verifies if the move is one space up and either to
the left or right one space
- is_valid_jump, which checks if the move is two spaces up and either left or
right two spaces.and overwrites

It also contains tests for the class as well.

*****************************************************************************'''

from Piece import *
class BlackPiece(Piece):
    
    def get_color(self):
        '''
        Method used to get the color of a specific piece object which is 
        defined in the Piece class.
        
        Parameters:
                   -- self
        Returns:
                  -- self.BLACK, which is the color of the black piece defined 
                  in the Piece class
        '''          
        return self.BLACK
    
    def display(self):
        '''
        Method used to display the red piece object on the board object in
        Board.py.
        
        Parameters:
                   -- self
        Returns:
                  -- "[b]", display on the board object
        '''                 
        return "[b]"

    def is_valid_move(self, new_x, new_y):
        '''
        Method used to check if the move is valid. Returns True or False
        based on if the coordinates are one space to the left or right
        and one space up from the current coordinates.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- True or False, depending on if conditions are met.
        '''        
        return self.y - 1 == new_y and (self.x + 1 == new_x 
                                        or self.x - 1 == new_x)

    def is_valid_jump(self, new_x, new_y):
        '''
        Method used to check if the jump is valid. Returns True or False
        based on if the coordinates are two spaces to the left or right
        and two spaces up from the current coordinates.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- True or False, depending on if conditions are met.
        '''           
        return self.y - 2 == new_y and (self.x + 2 == new_x 
                                        or self.x - 2 == new_x)
    


#===============================================================================
if __name__ == "__main__":
    piece = BlackPiece(4, 4)
    print((piece.x, piece.y), piece.display())
    
    for row in range(3, 6):
        for col in range(3,6):
            print(f"Move from (4, 4) to ({row}, {col})?", 
                  piece.is_valid_move(row, col))    