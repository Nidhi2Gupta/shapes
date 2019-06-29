#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:14:09 2019

@author: lavanyaguptairvine
"""

import turtle
def square (l):
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)

def star(size):
  turtle.begin_fill()
  for x in range (1,9):
    turtle.forward(size)
    turtle.left(225)
  turtle.end_fill()

def octagon(size, filled):
  if filled == True:
    turtle.begin_fill()
  for x in range(0,8):
    turtle.forward(70)
    turtle.left(45)
  if filled == True:
    turtle.end_fill()

square (50)
square(100)
square(200)
turtle.reset()
turtle.color("red")
star(200)
#turtle.reset()
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.color("yellow")
octagon(300, True)
turtle.speed(10)
turtle.color("green")
turtle.circle(50)
