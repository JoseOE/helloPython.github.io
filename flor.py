from turtle import *
import colorsys
import math

speed(0.50)
bgcolor("#7B7968")
# Genera los petalos
goto(0, -40)
h = 0
for i in range(16):
    for j in range(18):
        color("#F36AD8")
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte centrall de la flor
color("grey") 
shape("turtle")
fillcolor("#E1CF51")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()



done()