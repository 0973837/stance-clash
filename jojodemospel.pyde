import Dio, Jotaro, Polnareff, kokyoin, mrjoestar
import spelers
import Dobbelveld
import Stance_Clash, EvenementIDLE, EvenementKaart
from btn import *

WIDTH = 1920
HEIGHT = 1080





def setup():
    global scherm, backgroundImage, buttons, evenement
    fullScreen()
    Dio.setup()
    Jotaro.setup()
    Polnareff.setup()
    kokyoin.setup()
    mrjoestar.setup()
    spelers.setup()
    Dobbelveld.setup()
    Stance_Clash.setup()
    EvenementIDLE.setup()
    EvenementKaart.setup()
    size(WIDTH, HEIGHT)
    scherm = 0
    backgroundImage = loadImage("jojostart.jpg")
    
    
    
    

    
                   
def draw():
    global scherm, backgroundImage, buttons, evenement
    frameRate(12)
    #println(str(mouseX) + " : " + str(mouseY))
    #println(scherm)
    if scherm == 0:
        background(backgroundImage)
        # Titel
        textSize(100)
        fill(232,220, 220)
        text("Stance Clash", 650,200)
    
    
        textSize(50)
        fill(232, 220, 220, 50)
        rectFromDict(buttons[0])
    
    elif scherm == 1:
        spelers.draw()
    elif scherm == 2:
        Jotaro.draw()
    elif scherm == 3:
        Dio.draw()
    elif scherm == 4:
        mrjoestar.draw()
    elif scherm == 5:
        kokyoin.draw()
    elif scherm == 6:
        Polnareff.draw()
    elif scherm == 7:
        Dobbelveld.draw()
    elif scherm == 8:
        Stance_Clash.draw()
    elif scherm == 9:
        EvenementIDLE.draw()
    elif scherm == 10:
        EvenementKaart.draw()
    

def mousePressed():
    global scherm
    # Functie voor Start button
    if scherm == 0:
        # spelers scherm
        if checkButton(buttons[0]):
            scherm = 1
    elif scherm == 1:
        #jotaro scherm
        if checkButton(buttons[2]):
            scherm = 2
        #dio
        if checkButton(buttons[3]):
            scherm = 3
        #polnareff
        if checkButton(buttons[4]):
            scherm = 6
        #kokyoin
        if checkButton(buttons[5]):
            scherm = 5
        #mrjoestar
        if checkButton(buttons[6]):
            scherm = 4
        #back button
        if checkButton(buttons[1]):
            scherm = 0
        #dobbelsteenscherm
        if checkButton(buttons[7]):
            scherm = 7
    elif scherm == 2:
        if checkButton(buttons[1]):
            scherm = 1
    elif scherm == 3:
        if checkButton(buttons[1]):
            scherm = 1
    elif scherm == 4:
        if checkButton(buttons[1]):
            scherm = 1
    elif scherm == 5:
        if checkButton(buttons[1]):
            scherm = 1
    elif scherm == 6:
        if checkButton(buttons[1]):
            scherm = 1
    elif scherm == 7:
        if checkButton(buttons[1]):
            scherm = 1
        Dobbelveld.mousePressed()
        if checkButton(buttons[10]):
            scherm = 8
    elif scherm == 8:
        if checkButton(buttons[11]):
            scherm = 9
    elif scherm == 9:
        if checkButton(buttons[1]):
            scherm = 7
        if checkButton(buttons[12]):
            EvenementKaart.evenementkaart()
            scherm = 10
    elif scherm == 10:
        if checkButton(buttons[1]):
            scherm = 9
        
            
        




        
