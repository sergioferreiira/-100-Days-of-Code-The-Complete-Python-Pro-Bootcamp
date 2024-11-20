from turtle import Turtle , Screen , mode

mode("standard")
screen =Screen()
screen.listen()
screen.bgcolor("black")
screen.title("My SnAkE game")
screen.setup(width=600,height=600)

starting_positions = [(-20,0),(-40,0)]
snakes = []

# Função para criar as partes da cobra
def snakeCreation(snake):
    snake.shapesize(1)
    snake.shape("square")
    snake.color("white")
    snake.penup()

# Criando a cobra
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



x = 1

while game:
    # Momento em que lembrei sobre escopo
    screen.listen()

        # Teclas do jogo
    screen.onkey(turnSnakeUP, "w" )
    screen.onkey(turnSnakeRight, "d" )
    screen.onkey(turnSnakeDown, "s" )
    screen.onkey(turnSnakeLeft, "a" )
        #-------------------------------
    #------------------------------------

    headSnake.forward(x)
    
    positionOfMainSnake = headSnake.pos()
    for snake in snakes:
        snake.goto(positionOfMainSnake)

    snakePosition = headSnake.pos()
    if snakePosition[0] >= 299.00 or snakePosition[0] <= -299.00 or snakePosition[1] <= -299.00 or snakePosition[1] >= 299.00:
        game = False

####################################### END SNAKE MOVIMENT #############################################

        





screen.exitonclick()




