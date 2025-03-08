import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(254, 253, 250), (254, 252, 254), (247, 251, 254), (249, 253, 253), (207, 78, 137), (244, 147, 76), (235, 224, 89), (249, 47, 20), (81, 196, 235), (72, 204, 153), (186, 55, 33), (92, 110, 200), (243, 151, 201), (75, 91, 167), (55, 174, 45), (226, 128, 166), (36, 119, 59), (37, 77, 56), (8, 191, 212), (96, 41, 56), (251, 147, 1), (142, 188, 245), (22, 39, 96), (162, 36, 21), (48, 66, 43), (90, 51, 30), (97, 216, 249), (149, 67, 81), (33, 46, 102), (138, 218, 195)]

tim.setheading(225)
tim.forward(250)
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
