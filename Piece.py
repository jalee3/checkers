class Piece:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.RED = "R"
        self.BLACK = "B"
        self.PIECE = "-"
        
    def get_color(self):
        return self.PIECE
    
    def display(self):
        return "[P]"
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    
    def jump(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def is_valid_move(self, new_x, new_y):
        return False
    
    def is_valid_jump(self, new_x, new_y):
        return False
    
    def king(self):
        return False
    

if __name__ == "__main__":
    piece = Piece(4, 4)
    print((piece.x, piece.y), piece.get_color())
    
    for row in range(3, 6):
        for col in range(3,6):
            print(f"Move from (4, 4) to ({row}, {col})?", 
                  piece.is_valid_move(row, col))    