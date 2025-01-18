import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#f2baf7")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

turtle_instance.forward(50)
turtle_instance.left(90)
turtle_instance.forward(50)
turtle_instance.left(90)
turtle_instance.forward(50)
turtle_instance.left(90)
turtle_instance.forward(50)

'''
#by doing this with loop
for i in range (4):
    turtle_instance.left(90)
    turtle_instance.forward(50)
'''
turtle.done()