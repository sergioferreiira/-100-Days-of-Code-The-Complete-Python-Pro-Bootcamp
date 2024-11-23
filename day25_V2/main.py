import turtle , pandas

states = pandas.read_csv("day25_V2/50_states.csv")
counter = 49
gameMode = True
while gameMode:
    ########### screen #################
    
    screen = turtle.Screen()
    screen.title("U.S STATES")
    image = "day25_V2/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    
    ########### end screen #################
    
    writter = turtle.Turtle()
    writter.penup()
    writter.shapesize(0.1)


    ################## states validation #######################
    stateName = screen.textinput("U.S states","Name of states")
    formatedStateName = stateName.title()
    
    result = states.loc[states["state"] == formatedStateName]
    
    if not result.empty:
        writter.goto(x=result["x"].values[0], y=result["y"].values[0])
        writter.write(result["state"].values[0],align= "center", font= ("Arial", 8, "normal"))
        counter +=1 
        print(counter)
    else:
        print(f"The state {formatedStateName} doesn't exist.")
    
    ################## end states validation #######################
    if counter == len(states):
        gameMode = False

screen.exitonclick()


