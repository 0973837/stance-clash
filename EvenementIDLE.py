from btn import *

# Evenement scherm
def setup():
    global scherm
    scherm = 9

def draw():
    global scherm
    if scherm == 9:
        background(225)
        fill(150,200,225)
        textSize(100)
        text('EVENEMENT!', width/2 -340, height/4)
        #Back button
        textSize(40)
        x = buttons[1]
        rectFromDict(x)
        #Start Event button
        y = buttons[12]
        rectFromDict(y)
    
    elif scherm == 8:
        Stance_Clash.draw()    
