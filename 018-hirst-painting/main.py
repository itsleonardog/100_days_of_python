"""
IMPORTING COLOR FROM IMAGE

import colorgram

rgb_colors = []
colors = colorgram.extract('img.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
"""

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [
    (245, 239, 230),
    (227, 235, 243),
    (247, 230, 238),
    (124, 180, 210),
    (234, 243, 238),
    (198, 174, 16),
    (29, 119, 167),
    (176, 14, 45),
    (235, 150, 76),
    (236, 204, 90),
    (217, 124, 163),
    (26, 144, 74),
    (215, 80, 123),
    (9, 171, 210),
    (212, 61, 27),
    (237, 77, 45),
    (245, 157, 187),
    (64, 21, 53),
    (12, 183, 150),
    (13, 31, 75),
    (161, 57, 106),
    (76, 27, 22),
    (129, 209, 233),
    (161, 192, 164),
    (15, 48, 132),
    (102, 116, 181),
    (250, 159, 152),
    (168, 24, 19),
    (121, 216, 209),
    (3, 88, 57)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
