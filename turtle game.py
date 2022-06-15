#ASHLY DANIEL JOHN
#SFIT
from turtle import *
from random import randint
import turtle

bgcolor("orange")    #BACKGROUND COLOR

penup()          #TITLE
goto(-140,180)
write("TURTLE RACE",font=("Castellar", 30, "normal"))

penup()         #START
goto(-225,120)
write("START",font=("elephant", 12, "normal"))

penup()         #FINISH
goto(-229,-25)
write("FINISH",font=("elephant", 12, "normal"))

speed(0)
penup()
goto(-140,140)

for step in range(16):
    write(step)
    right(90)
    for num in range (8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
    
forward(20)
ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()


bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()


lob=Turtle()
lob.color('green')
lob.shape('turtle')
lob.penup()
lob.goto(-160,40)
lob.pendown()


nob=Turtle()
nob.color('yellow')
nob.shape('turtle')
nob.penup()
nob.goto(-160,10)
nob.pendown()

for turn in range (100):
    ada.forward(randint(1,6))
    bob.forward(randint(1,6))
    lob.forward(randint(1,6))
    nob.forward(randint(1,6))

for turn in range (1) :
    ada.left(180)
    bob.left(180)
    lob.left(180)
    nob.left(180)


for turn in range (100):
    ada.forward(randint(1,6))
    bob.forward(randint(1,6))
    lob.forward(randint(1,6))
    nob.forward(randint(1,6))





