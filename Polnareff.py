from btn import *


def setup():
    #global achtergrond
    size(1920,1080)
    #achtergrond = loadImage("polnarefffoto.jpg")

def draw():
    #global achtergrond
    background("#938887")
    textSize(40)
    fill(5,5,5)
    text("Mag 2x gooien", 150, 300)
    textSize(40)
    fill(5,5,5)
    text("Maar trekt 3 stappen van de gegooide stappen af", 150, 400) 
    textSize(40)
    fill(5,5,5)
    text("Als je minder/gelijk aan 3 gooit, neem 2 stappen", 150, 500)
    fill(255)
    x = buttons[1]
    rectFromDict(x)
