from turtle import Turtle , Screen , mode

mode("standard")
screen =Screen()
screen.listen()
screen.bgcolor("black")
screen.title("My SnAkE game")
screen.setup(width=600,height=600)

starting_positions = [(-20,0),(-40,0)]
snakes = []


def snakeCreation(snake):
    snake.shapesize(2)
    snake.shape("square")
    snake.color("white")
    snake.penup()

for position in starting_positions:
    newSnake = Turtle()
    snakeCreation(newSnake)
    newSnake.goto(position)
    snakes.append(newSnake)

    headSnake =Turtle()
    snakeCreation(headSnake)


wanna_play = str(screen.textinput("Wanna play?", "YES / NO"))
if wanna_play.lower() == "yes":
    game = True
else:
    game = False
####################################### SNAKE MOVIMENT #############################################
def turnSnakeUP():
    headSnake.setheading(90)
def turnSnakeRight():
    headSnake.setheading(0)
def turnSnakeDown():
    headSnake.setheading(270)
def turnSnakeLeft():
    headSnake.setheading(180)

x = 3

while game:
    headSnake.forward(x)
    screen.onkey(turnSnakeUP, "w" or "W")
    screen.onkey(turnSnakeRight, "d" or "D")
    screen.onkey(turnSnakeDown, "s" or "S")
    screen.onkey(turnSnakeLeft, "a" or "A")

    snakePosition = newSnake.pos()

    if snakePosition[0] >= 299.00:
        game = False
    elif snakePosition[0] <= -299.00:
        game = False
    elif snakePosition[1] <= -299.00:
        game = False
    elif snakePosition[1] >= 299.00:
        game = False

####################################### END SNAKE MOVIMENT #############################################

        





screen.exitonclick()




