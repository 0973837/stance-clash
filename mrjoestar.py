from btn import *


def setup():
    size(1920,1080)

def draw():
    background("#61FF5A")
    textSize(40)
    fill(5,5,5)
    text("Kan 1x per beurt de kaart die de speler van de stapel", 150, 300)
    textSize(40)
    fill(5,5,5)
    text("pakt wisselen met de eerstvolgende kaart op de stapel", 150, 350) 
    textSize(40)
    fill(5,5,5)
    text("Maar heeft altijd -1 power", 150, 450)
    fill(255)
    x = buttons[1]
    rectFromDict(x)
