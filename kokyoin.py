from btn import *


def setup():
    size(1920, 1080)


def draw():
    background("#938887")
    textSize(40)
    fill(5,5,5)
    text("Mag kiezen hoeveel stappen als het maar onder de", 150, 300)
    textSize(40)
    fill(5,5,5)
    text("gegooide stappen is", 150, 350) 
    textSize(40)
    fill(5,5,5)
    text("Maar moet 2 stappen van de gegooide stappen aftrekken", 150, 450)
    fill(255)
    x = buttons[1]
    rectFromDict(x)
