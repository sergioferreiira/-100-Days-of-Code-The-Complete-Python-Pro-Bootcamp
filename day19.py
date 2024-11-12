from turtle import Turtle , Screen
import random
################# instances and presets #################

screen = Screen()
screen.setup(width=800,height=600)

turtleBet = screen.textinput("Turtle Race", "who will win? \n red\n black \n blue\n pink\n yellow?")

def instanceTurtle(name, turtleColor, startPosition):
    name.color("white", turtleColor)
    name.shape("turtle")
    name.speed(7)
    name.shapesize(2)
    name.penup()
    name.goto(startPosition)
    name.pendown()

def createRandomTurtle():
    colorsList = ["red", "black", "blue", "pink", "yellow"]
    startRandomPositions = [
        (-390, 0),
        (-390, 100),
        (-390, -100),
        (-390, 200),
        (-390, -200)
    ]
    
    
    randomNames = [Turtle() for _ in range(5)]
    
    for turtle, color, position in zip(randomNames, colorsList, startRandomPositions):
        instanceTurtle(name=turtle, turtleColor=color, startPosition=position)

    x = True
    while x:
        for turtle in randomNames:
            turtle.forward(random.randint(7, 27))
            z, w = turtle.pos()  # Obtém a posição atual de cada tartaruga

            # Verifica se a tartaruga atingiu ou passou de x = 400
            if z >= 400:
                print(f"A tartaruga de cor {turtle.color()[1]} chegou a (400, {w})!")
                turtleWinner = turtle.color()[1]
                if turtleWinner == turtleBet:
                    turtle.write("You win")
                else:
                    turtle.write("You lose")

                x = False
                break  # Sai do loop `for` se uma tartaruga atinge x = 400



createRandomTurtle()



################# end Instances #################

# turtleList = [t1,t2,t3,t4,t5]
# x = 0
# while x != 30:
#   for turtle in turtleList:
#     turtle.forward(random.randint(10,30))
#   x+=1

# for turtle in turtleList:
#   print(turtle.position())


screen.listen()



















screen.exitonclick()







