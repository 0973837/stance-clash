#spelers scherm
from btn import *

def setup():
    global scherm, jotaroImg, dioImg, polnareffImg, kokyoinImg, mrjoestarImg, achtergrondImg
    size(1920,1080)
    scherm = 1
    jotaroImg = loadImage("jotarofoto.jpg")
    dioImg = loadImage("diofoto.jpg")
    polnareffImg = loadImage("polnarefffoto.jpg")
    kokyoinImg = loadImage("kokyoinfoto.jpg")
    mrjoestarImg = loadImage("MRJoestarfoto.jpg")
    achtergrondImg = loadImage("PlayerBackground.jpg")

def draw():
    global scherm
    background(achtergrondImg)
    fill(255)
    image(jotaroImg, 150, 100, 250, 200)
    image(dioImg, 825, 100, 250, 200)
    image(polnareffImg, 1450, 100, 250, 200)
    image(kokyoinImg, 500, 400, 250, 200)
    image(mrjoestarImg, 1150, 400, 250, 200)
    textSize(50)
    text("JOTARO", 180, 350)
    text("DIO", 900, 350)
    text("POLNAREFF", 1430, 350)
    text("KAKYOIN", 513, 650)
    text("MR JOESTAR", 1125, 650)
    textSize(40)
    x = buttons[1]
    rectFromDict(x)
    fill("#FFFFFF")
    y = buttons[7]
    rectFromDict(y)
