import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#f2baf7")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

#star turtle
for i in range (5):
    turtle_instance.left(144)
    turtle_instance.forward(100)
turtle.done()