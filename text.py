import turtle as blah
import random
t=blah.Turtle()
blah.colormode(255)
color_list=[(244, 240, 243), (236, 242, 238), (196, 158, 123), (135, 96, 67), (137, 165, 188), (230, 209, 128), (147, 181, 155), (73, 100, 133), (77, 111, 90), (209, 95, 64), (183, 155, 162), (164, 135, 78), (91, 149, 112), (222, 177, 186), (230, 176, 164), (179, 200, 184), (119, 94, 106), (178, 189, 210), (102, 125, 162), (35, 64, 105), (182, 195, 198), (153, 114, 125), (46, 76, 52), (95, 139, 147), (76, 71, 46), (40, 65, 45), (33, 54, 78), (66, 56, 40)]
new_color_list=[]
random_color=random.choice(color_list)


blah.forward(20)
blah.setheading(180)

for _ in range(10):
    t.dot(10, random_color)
    t.forward(20)



screen=blah.Screen()
screen.exitonclick()