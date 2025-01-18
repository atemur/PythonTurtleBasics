import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#f2baf7")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

#polygon
num_sides = 5
angle = 360.0 / num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)
turtle.done()