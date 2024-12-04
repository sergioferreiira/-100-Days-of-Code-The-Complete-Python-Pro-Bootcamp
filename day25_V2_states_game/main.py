import turtle , pandas

states = pandas.read_csv("day25_V2/50_states.csv")
counter = 0
gameMode = True
while gameMode:
    
    ########### screen #################
    
    screen = turtle.Screen()
    screen.title("U.S STATES")
    image = "day25_V2/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    
    ########### end screen #################
    def capturar_click(x, y):
        print(f"Você clicou nas coordenadas: x = {x}, y = {y}")
    screen.onscreenclick(capturar_click)
    
    
    writter = turtle.Turtle()
    writter.penup()
    writter.shapesize(0.1)
    writter.hideturtle()
    
    
    # ive tried use a new turtle to count the score but when i saw the video the counter was in the title of screen text input 
    # so ill let here just for remember if necessary
    
    # counter_turtle = turtle.Turtle()
    # counter_turtle.hideturtle() 
    # counter_turtle.penup()  
    # counter_turtle.goto(x = -353.0, y = 289.0) 
    # counter_turtle.write(f"Contador: {counter}", align="left", font=("Arial", 24, "normal"))

    ################## states validation #######################
    stateName = screen.textinput(f"{counter}/50 U.S states", "Name of states")
    formatedStateName = stateName.title()
    
    result = states.loc[states["state"] == formatedStateName]
    
    if not result.empty:
        writter.goto(x=result["x"].values[0], y=result["y"].values[0])
        writter.write(result["state"].values[0],align= "center", font= ("Arial", 8, "normal"))
        # screen.update()  # its necessary to chance the number of counter
        # counter_turtle.clear()
        counter +=1 
        print(counter)
    else:
        print(f"The state {formatedStateName} doesn't exist.")
    
    ################## end states validation #######################
    if counter == len(states):
        gameMode = False

screen.exitonclick()


