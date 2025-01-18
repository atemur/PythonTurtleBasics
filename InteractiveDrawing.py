import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(50)
def turtle_left():
    turtle_instance.left(90)
def turtle_right():
    turtle_instance.right(90)
def turtle_back():
    turtle_instance.back(50)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="Up")
drawing_board.onkey(fun=turtle_left, key="Left")
drawing_board.onkey(fun=turtle_right, key="Right")
drawing_board.onkey(fun=turtle_back, key="Down")

turtle.mainloop()