import turtle as blah
import random

t = blah.Turtle()

color_list = [(244, 240, 243), (236, 242, 238), (196, 158, 123), (135, 96, 67), (137, 165, 188), (230, 209, 128),
              (147, 181, 155), (73, 100, 133), (77, 111, 90), (209, 95, 64), (183, 155, 162), (164, 135, 78),
              (91, 149, 112), (222, 177, 186), (230, 176, 164), (179, 200, 184), (119, 94, 106), (178, 189, 210),
              (102, 125, 162), (35, 64, 105), (182, 195, 198), (153, 114, 125), (46, 76, 52), (95, 139, 147),
              (76, 71, 46), (40, 65, 45), (33, 54, 78), (66, 56, 40)]

t.speed("fastest")
blah.hideturtle()


start_x = -10 * 20 / 2  
start_y = 10 * 20 / 2   

t.penup()
t.goto(start_x, start_y)  
t.pendown()


for row in range(10):
    for col in range(10):
        random_color = random.choice(color_list)  
        hex_color = '#%02x%02x%02x' % random_color
        t.dot(10, hex_color)
        t.penup()
        t.forward(20)
        t.pendown()
    t.penup()
    t.goto(start_x, t.ycor() - 20)  
    t.pendown()

screen = blah.Screen()
screen.exitonclick()

