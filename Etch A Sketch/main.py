from turtle import Turtle, Screen

jerry = Turtle()
screen = Screen()


def move_forwards():
    jerry.forward(10)


def move_backwards():
    jerry.backward(10)


def turn_left():
    new_heading = jerry.heading() + 10
    jerry.setheading(new_heading)


def turn_right():
    new_heading = jerry.heading() - 10
    jerry.setheading(new_heading)


def clear():
    jerry.clear()
    jerry.penup()
    jerry.home()
    jerry.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
