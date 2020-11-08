""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""


def function(original_function):
    def inner_function():
        return original_function()
    return inner_function

def display():
    print("display run")

var = function(display)

var()
