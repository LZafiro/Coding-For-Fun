# Turtle Fractal Tree
# Luiz Felipe Raveduti Zafiro

import turtle

lenght = 500
height = 500

turtle.screensize(lenght, height)

# Definition of the initial setup for the canvas
def setup():
    
    brush = turtle.Turtle()
    brush.color('Gray')
    brush.left(90)
    brush.penup()
    brush.setpos(0, -240)
    brush.pendown()
    brush.speed(150)
    brush.pensize(2)
    return brush

# Recursive function for drawning a fractal tree
def fractal_tree_rec(brush, size):

    if(size < 10):
        return

    brush.forward(size)
    brush.left(30)
    fractal_tree_rec(brush, size * 3 / 4)
    brush.right(60)
    fractal_tree_rec(brush, size * 3 / 4)
    brush.left(30)
    brush.backward(size)
    

brush = setup()
fractal_tree_rec(brush, 100)
