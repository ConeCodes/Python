"""
Name:         ch7Assignment.py
Purpose:      To draw a smiley face.
Author:       Dalton Cone
"""
from turtle import *
pensize(3)
pu()
bk(160)
pd()
circle(66)
fillcolor("blue")
begin_fill()
circle(33)
end_fill()

pu()
fd(160)
pd()

circle(66)
fillcolor("blue")
begin_fill()
circle(33)
end_fill()

pu()
bk(80)
rt(90)
fd(50)
lt(90)
pd()

fillcolor("red")
begin_fill()
circle(25)
end_fill()

pu()
goto(-260, -50)
pd()

rt(90)
fd(50)
lt(90)
fd(350)
lt(90)
fd(50)

pu()
rt(90)
fd(30)
lt(90)
pd()
circle(250)
done() 
