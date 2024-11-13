from turtle import Turtle , Screen

screen =Screen()
screen.listen()
screen.bgcolor("black")
screen.title("My SnAkE game")

gameSnake = Turtle()

def instanceFollowersTurtles(turtle):
    turtle.shape("square")
    turtle.shapesize(3)
    turtle.color("white")



def moveForward():
    gameSnake.setheading(90)
    while True:
        gameSnake.forward(1)
        


screen.onkey(moveForward, 'w')



screen.exitonclick()




