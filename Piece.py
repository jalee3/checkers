'''*****************************************************************************
Jason Lee
Wed, Oct 02, 2020
Checkers

This library contains all the info needed to create a checkers piece for 
the textbased checkers game. The Piece class contains x and y attributes to save 
their coordinates as well as a color attribute to determine the color of the 
piece.

The methods contained within this file are:
- get_color, which returns the pieces color
- display, which displays the piece on the board object
- move, which sets the self.x and self.y attributes to the new x and y
values
- jump, which sets the self.x and self.y attributes to the new x and y
values
- is_valid_move, to check if the move is valid
- is_valid_jump, to check if a jump is valid.

It also contains tests for the class as well.

*****************************************************************************'''

class Piece:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.RED = "R"
        self.BLACK = "B"
        self.PIECE = "-"
        
    def get_color(self):
        '''
        Method used to get the color of a specific piece object which is 
        defined in __init__.
        
        Parameters:
                   -- self
        Returns:
                  -- self.PIECE, which is the color of the piece
        '''         
        return self.PIECE
    
    def display(self):
        '''
        Method used to display the piece object on the board object in
        Board.py.
        
        Parameters:
                   -- self
        Returns:
                  -- "[P]", display on the board object
        '''        
        return "[P]"
    
    def move(self, new_x, new_y):
        '''
        Method used to move the piece object on the board object in
        Board.py. Sets the piece objects coordinates to the new x and 
        y coordinates passed in as an argument
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- None
        '''        
        self.x = new_x
        self.y = new_y

    
    def jump(self, new_x, new_y):
        '''
        Method used for the jump movement for the piece object on the board 
        object in Board.py. Sets the piece objects coordinates to the new x and 
        y coordinates passed in as an argument
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- None
        '''
        self.x = new_x
        self.y = new_y

    def is_valid_move(self, new_x, new_y):
        '''
        Method used to check if the move is a valid move. For the Piece object
        it returns False.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- False
        '''        
        return False
    
    def is_valid_jump(self, new_x, new_y):
        '''
        Method used to check if the jump is valid. For the Piece object
        it returns False.
        
        Parameters:
                   -- new_x, new x coordinate for the piece object 
                   -- new_y, new y coordinate for the piece object 
        Returns:
                  -- False
        '''          
        return False
    
#===============================================================================
if __name__ == "__main__":
    piece = Piece(4, 4)
    print((piece.x, piece.y), piece.get_color())
    
    for row in range(3, 6):
        for col in range(3,6):
            print(f"Move from (4, 4) to ({row}, {col})?", 
                  piece.is_valid_move(row, col))  