#spelers scherm
from btn import *

def setup():
    global scherm, jotaroImg, dioImg, polnareffImg, kokyoinImg, mrjoestarImg
    size(1280, 725)
    scherm = 1
    jotaroImg = loadImage("jotarofoto.jpg")
    dioImg = loadImage("diofoto.jpg")
    polnareffImg = loadImage("polnarefffoto.jpg")
    kokyoinImg = loadImage("kokyoinfoto.jpg")
    mrjoestarImg = loadImage("MRJoestarfoto.jpg")

def draw():
    global scherm
    background("#938887")
    fill(255)
    image(jotaroImg, 150, 100, 150, 100)
    image(dioImg, 550, 100, 150, 100)
    image(polnareffImg, 950, 100, 150, 100)
    image(kokyoinImg, 350, 300, 150, 100)
    image(mrjoestarImg, 750, 300, 150, 100)
    x = buttons[1]
    rectFromDict(x)
