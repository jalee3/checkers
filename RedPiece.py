from Piece import *
class RedPiece(Piece):
    
    def get_color(self):
        return self.RED
    
    def display(self):
        return "[r]"
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def jump(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def is_valid_move(self, new_x, new_y):
        return self.y + 1 == new_y and (self.x + 1 == new_x 
                                        or self.x - 1 == new_x)

    def is_valid_jump(self, new_x, new_y):
        return self.y + 2 == new_y and (self.x + 2 == new_x 
                                        or self.x - 2 == new_x) 
    
    def king(self):
        if self.y == 7:
            return "[R]"
        else:
            return False        


if __name__ == "__main__":
    piece = RedPiece(4, 4)
    print((piece.x, piece.y), piece.get_color())
    
    for row in range(3, 6):
        for col in range(3,6):
            print(f"Move from (4, 4) to ({row}, {col})?", 
                  piece.is_valid_move(row, col))