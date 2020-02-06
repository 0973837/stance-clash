import random
from btn import *


def setup():
    global kaart, scherm, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10
    scherm = 10
    E1 = loadImage('E1.png')
    E2 = loadImage('E2.png')
    E3 = loadImage('E3.png')
    E4 = loadImage('E4.png')
    E5 = loadImage('E5.png')
    E6 = loadImage('E6.png')
    E7 = loadImage('E7.png')
    E8 = loadImage('E8.png')
    E9 = loadImage('E9.png')
    E10 = loadImage('E10.png')
    
    kaart = []

def draw():
    global buttons, kaart
    
    textSize(40)
    x = buttons[1]
    rectFromDict(x)
    textSize(75)
    y = buttons[14]
    rectFromDict(y)
    print kaart
    for i in kaart:
        image(i[0],i[1],i[2],i[3],i[4])



    
def evenementkaart():
    global evenementlist, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, randomlist, kaart
    evenementlist = [1,2,3,4,5,6,7,8,9,10]
    randomlist = random.choice(evenementlist)
    if randomlist == 1:
        kaart = [(E1, 725, 250, 400, 600)]
    elif randomlist == 2:
        kaart = [(E2, 725, 250, 400, 600)]
    elif randomlist == 3:
        kaart = [(E3, 725, 250, 400, 600)]
    elif randomlist == 4:
        kaart = [(E4, 725, 250, 400, 600)]
    elif randomlist == 5:
        kaart = [(E5, 725, 250, 400, 600)]
    elif randomlist == 6:
        kaart = [(E6, 725, 250, 400, 600)]
    elif randomlist == 7:
        kaart = [(E7, 725, 250, 400, 600)]
    elif randomlist == 8:
        kaart = [(E8, 725, 250, 400, 600)]
    elif randomlist == 9:
        kaart = [(E9, 725, 250, 400, 600)]
    elif randomlist == 10:
        kaart = [(E10, 725, 250, 400, 600)]
        
