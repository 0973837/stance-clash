from btn import *

def setup():
    #global achtergrond
    size(1920,1080)
    #achtergrond = loadImage("jotarofoto.jpg")

def draw():
    #global achtergrond
    background("#5AF8FF")
    textSize(40)
    fill(5,5,5)
    text("Kan om de 3 beurten een kaart pakken", 150, 300)
    textSize(40)
    fill(5,5,5)
    text("Maar pakt altijd kaarten van de onderkant", 150, 400)
    fill(255)
    x = buttons[1]
    rectFromDict(x)
