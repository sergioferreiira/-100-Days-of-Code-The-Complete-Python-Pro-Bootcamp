import turtle , pandas

states = pandas.read_csv("day25_V2/50_states.csv")

while True:
 stateName = input(str("type the name of the state: "))

 resultado = states.loc[states["state"] == stateName]


 print(resultado)
# print(states)

# screen = turtle.Screen()
# screen.title("U.S STATES")
# image = "day25_V2/blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)







# screen.exitonclick()