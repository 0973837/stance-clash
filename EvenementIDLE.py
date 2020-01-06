# Evenement scherm

def draw():
    scherm = 1
    if scherm == 1:
        background(225)
        fill(150,200,225)
        text('EVENEMENT!', width/2 - 250, height/4)
        #Back button
        rect(width/2 - 200, height/2 + 50, 400, 200)
        fill(170)
        text('Back',  width/4 + 350,height/2 + 175)
        #Start Event button
        fill(150,200,225)
        rect(width/2 - 200, height/2 - 200, 400, 200)
        fill(170)
        text('Start event', width/4 + 300,height/2 - 75)
    
    elif scherm == 0:
        Stance_Clash.draw()    
