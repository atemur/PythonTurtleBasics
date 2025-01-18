import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle Spiral Helix")

turtle_instance = turtle.Turtle()
turtle.speed("fastest")
turtle_instance.color("blue")

turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(25):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()#we can use this instead of turtle.done
#turtle.done()