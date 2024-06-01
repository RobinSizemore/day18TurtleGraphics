import turtle
import random
# import colorgram

#
# get colors from file.
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

rgb_colors = [(213, 154, 104), (15, 20, 73),
              (234, 225, 101), (51, 86, 145), (113, 171, 211), (168, 80, 48), (49, 29, 20), (193, 90, 123),
              (211, 86, 63), (55, 117, 51), (27, 44, 129), (111, 37, 64), (23, 45, 29), (156, 62, 88), (196, 135, 170),
              (121, 197, 161), (139, 33, 26), (64, 27, 39), (152, 211, 197), (98, 112, 192), (31, 89, 46), (84, 81, 32),
              (65, 161, 115), (150, 212, 220), (165, 186, 223), (226, 175, 163)]

# setup screen
screen = turtle.Screen()
screen.setup(750, 750, 2750, 1600)  # positioning is because of my weird monitor setup
turtle.colormode(255)

# setup turtle
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("black")
bob.speed("fastest")
bob.penup()

for x in range(-250, 300, 50):
    for y in range(-250, 300, 50):
        bob.goto(x, y)
        bob.dot(20, random.choice(rgb_colors))

screen.exitonclick()



