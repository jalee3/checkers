from graphics import *

win = None
PIECES_PER_SIDE = 12

def alternate_square(y, c):
    global win
    
    xl, xr = 10, 100
    for i in range(8):
        rect = square(y, xl, xr)
        xl += 90
        xr += 90       
        rect.setFill(c)
        rect.draw(win)
        c = alternate_color(c)        


def alternate_color(c): 
    if c == color_rgb(255, 0, 0):
        c = color_rgb(0, 0, 0)
    else:
        c = color_rgb(255, 0, 0)
    return c


def square(y, xuleft, xlright):
    rect = Rectangle(Point(xuleft, y - 80), Point(xlright, y + 10))
    return rect


def pieces_on_board():
    global win
    
    
    x, y = 55, 55
    L = pieces(x, y)
    x = 145
    y += 90
    L = pieces(x, y)
    x = 55
    y += 90
    L = pieces(x, y)
        
        
def pieces(x, y):      
    for i in range(PIECES_PER_SIDE//3):
        b_piece = black_piece(x, y)
        b_piece.draw(win)
        
        r_piece = red_piece(x, y)
        r_piece.draw(win)
        x += 180

def black_piece(x, y):
    circle = Circle(Point(x, y), 38)
    circle.setFill(color_rgb(50,50,50))
    return circle


def red_piece(x, y):
    if x < 685:
        circle = Circle(Point(x + 90, y + 450), 38)
        circle.setFill(color_rgb(255, 0, 0))
    else:
        x = 55
        circle = Circle(Point(x, y + 450), 38)
        circle.setFill(color_rgb(255, 0, 0))
    return circle



def board(s, c):
    global win
    y_coordinate = 90
    win = GraphWin("Checkers", 900, 800)
    
    for i in range(8):
        section = alternate_square(y_coordinate, c)      
        y_coordinate += 90
        c = alternate_color(c)
    pieces_on_board()
    win.getMouse()
    win.close()
    
    
board(8, color_rgb(0, 0, 0))