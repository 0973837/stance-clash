from btn import *


def setup():
    #global achtergrond
    size(1920, 1080)
    #achtergrond = loadImage("diofoto.jpg")

def draw():
    #global achtergrond
    background("#938887")
    textSize(40)
    fill(5,5,5)
    text("Heeft altijd +3 power", 150, 300)
    textSize(40)
    fill(5,5,5)
    text("Maar moet altijd een stap achteruit doen na het gooien", 150, 400)
    fill(255)
    x = buttons[1]
    rectFromDict(x)
