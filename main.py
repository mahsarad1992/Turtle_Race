import turtle
import random


colors = ["magenta3", "PaleTurquoise4", "DeepSkyBlue", "gold", "OrangeRed", "LightSalmon", "azure4"]
color_number = []
for i in range(0, 7):
    color_number.append(i+1)


def color_assigner():
    colors_dict = {}
    for index in color_number:
        colors_dict[index] = colors[index-1]
    print(colors_dict)
    return colors_dict

screen = turtle.Screen()
screen.setup(width=500, height=400)
color_assigner()

turtles = {}
for _ in range(1, 8):
    turtles[_] = turtle.Turtle("turtle")
print(turtles)
x = -235
y = -150
for i in turtles:
    turtles[i].penup()
    turtles[i].color(colors[i-1])
    turtles[i].goto(x, y)
    y += 50
user_bet = screen.textinput(title="winner", prompt="which turtle do you think will win?\nfrom 1 at the top to 7 the very bottom")
game_is_on = True
while game_is_on:
    for i in turtles:
        turtles[i].forward(random.randrange(0, 17, 4))
        if turtles[i].xcor() > 210:
            print(f"turtle {i} is winner")
            if int(i) == int(user_bet):
                print("you Win")
            else:
                print("you Lose")
            game_is_on = False

screen.exitonclick()