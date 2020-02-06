import random
from btn import *

#MainScreen
def setup():
    global mrjoestarDead, jotaroDead, polnareffDead, kakyoinDead, dioDead, hart, selectedNumber, buttons, currentNumber1, currentNumber2, currentNumber3, currentNumber4, currentNumber5, DobbelsteenImg, Menacing, aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel_N, DobbelN, Dobbel_D, DobbelD, Dobbel_P, DobbelP, Dobbel_K, DobbelK, DobbelK1, Dobbel, Kruis, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6, Dice_To_Draw                                         
    fullScreen()
#levensteller
    hart = loadImage("hart.png")
    selectedNumber = 0
    currentNumber1 = 3
    currentNumber2 = 3
    currentNumber3 = 3
    currentNumber4 = 3
    currentNumber5 = 3
    dioDead = False
    kakyoinDead = False
    polnareffDead = False
    jotaroDead = False
    mrjoestarDead = False
#Variables
    DobbelsteenImg = loadImage("Dice.png")
    
    Menacing = loadImage("Menacing.png")
    
    TurnTeller = 0
    
    Background = loadImage("Jojo turn background.jpg")
    
    Dice_6 = loadImage("Dice #6.png")
    Dice_5 = loadImage("Dice #5.png")
    Dice_4 = loadImage("Dice #4.png")
    Dice_3 = loadImage("Dice #3.png")
    Dice_2 = loadImage("Dice #2.png")
    Dice_1 = loadImage("Dice #1.png")
    Kruis = loadImage("kruis.png")
    
    
    
    Dio = False
    Jotaro = False
    Kakyion = False
    Polnareff = False
    Mrjoestar = False
    
    Dobbel = 0
    
    aap1 = False
    aap2 = False
    aap3 = False
    aap4 = False
    aap5 = False
    
#dobbelstenen die gekent moeten worden 
    Dice_To_Draw = []
    
#vakje dobbelstenen
    fill(255)
    stroke(3)
    rect(((width//2)-270), ((height//2)-410), 520, 170)
    
    
def draw():
    global buttons, selectedNumber, dioDead, kakyoinDead, polnareffDead, jotaroDead, mrjoestarDead, DobbelsteenImg,  aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel, Menacing
    background(Background)
    fill("#FFFFFF")
    x = buttons[8]
    rectFromDict(x)
    y = buttons[9]
    rectFromDict(y)
    textSize(40)
    z = buttons[1]
    rectFromDict(z)
    o = buttons[10]
    rectFromDict(o)
################################################################################################ DOBBEL ONDERDEEL ########################################################################################################################
    
#De dobbel knop
    noFill()
    noStroke()
    rect(((width//2)-150), ((height//2)-150), 300, 300,)
    
#Dobbelstenen vak
    image(Menacing, ((width//2)-270), ((height//2)-420), 65, 170)
    image(Menacing, ((width//2)+200), ((height//2)-420), 65, 170)

#Afbeelding in de dobbel knop
    image(DobbelsteenImg, ((width//2)-190), ((height//2)-190),380, 380)
    
    for i in Dice_To_Draw:
        image(i[0],i[1],i[2],i[3],i[4])
    
#    if mouseX > ((width//2)-150) and mouseX < ((width//2)+150) and mouseY > ((height//2)-150) and mouseY < ((height//2)+150):
#        tint(127, 0, 0)
#        image(DobbelsteenImg, ((width//2)-150), ((height//2)-150),300, 300)
#    else:
#        image(DobbelsteenImg, ((width//2)-150), ((height//2)-150),300, 300)




################################################################################################# TURN ONDERDEEL ##########################################################################################################################
    
#Turn veld
    fill(250)
    stroke(3)
    rect(50, 50, 300, 300,)
    
#Beurten systeem
    if TurnTeller > 5:
        TurnTeller = 1
        
    if TurnTeller == 1:
        aap1 = True
        aap2 = False
        aap3 = False
        aap4 = False
        aap5 = False
    elif TurnTeller == 2:
        aap1 = False
        aap2 = True
        aap3 = False
        aap4 = False
        aap5 = False
    elif TurnTeller == 3:
        aap1 = False
        aap2 = False
        aap3 = True
        aap4 = False
        aap5 = False
    elif TurnTeller == 4:
        aap1 = False
        aap2 = False
        aap3 = False
        aap4 = True
        aap5 = False
    elif TurnTeller == 5:
        aap1 = False
        aap2 = False
        aap3 = False
        aap4 = False
        aap5 = True
    else:
        aap1 = False
        aap2 = False
        aap3 = False
        aap4 = False
        aap5 = False

#Text in turn veld
    textSize(45)
    textAlign(200, 100)
    fill(0)
    if aap1 == True: 
        text("Player 1", 150, 90)
        text("Player 2", 75, 150)
        text("Player 3", 75, 210)
        text("Player 4", 75, 270)
        text("Player 5", 75, 330)
    elif aap2 == True:
        text("Player 1", 75, 90)
        text("Player 2", 150, 150)
        text("Player 3", 75, 210)
        text("Player 4", 75, 270)
        text("Player 5", 75, 330)
    elif aap3 == True:
        text("Player 1", 75, 90)
        text("Player 2", 75, 150)
        text("Player 3", 150, 210)
        text("Player 4", 75, 270)
        text("Player 5", 75, 330)
    elif aap4 == True:
        text("Player 1", 75, 90)
        text("Player 2", 75, 150)
        text("Player 3", 75, 210)
        text("Player 4", 150, 270)
        text("Player 5", 75, 330)
    elif aap5 == True:
        text("Player 1", 75, 90)
        text("Player 2", 75, 150)
        text("Player 3", 75, 210)
        text("Player 4", 75, 270)
        text("Player 5", 150, 330)
    else:
        text("Player 1", 75, 90)
        text("Player 2", 75, 150)
        text("Player 3", 75, 210)
        text("Player 4", 75, 270)
        text("Player 5", 75, 330)

#Charachter text box
    fill(255)
    stroke(3)
    rect(((width//2)-110), ((height//2)+210), 250, 50,)

#Charachter text
    textSize(45)
    textAlign(200, 100)
    fill(0)
    if aap1 == True: 
        text("Dio", ((width/2)-80), ((height/2)+250))
    elif aap2 == True:
        text("Kakyion", ((width/2)-80), ((height/2)+250))
    elif aap3 == True:
        text("Polnareff", ((width/2)-80), ((height/2)+250))
    elif aap4 == True:
        text("Jotaro", ((width/2)-80), ((height/2)+250))
    elif aap5 == True:
        text("Mrjoestar", ((width/2)-80), ((height/2)+250))
        

    
#Text end/start turn knop
    textSize(15)
    fill(0)
    if TurnTeller == 0:
        text("START", 403, 70)
        text("GAME", 405, 90)
    else:
        text("END", 405, 70)
        text("TURN", 405, 90)

#Dobbel indicatie test
#    if Dio == True:
#        fill(50)
#        rect(((width//2)-150), ((height//2)-150), 40, 40,)
#    elif Kakyion == True:
#        fill(100)
#        rect(((width//2)-150), ((height//2)-150), 40, 40,)
#    elif Polnareff == True:
#        fill(150)
#        rect(((width//2)-150), ((height//2)-150), 40, 40,)
#    elif Jotaro == True:
#        fill(200)
#        rect(((width//2)-150), ((height//2)-150), 40, 40,)
#    elif Mrjoestar == True:
#        fill(250)
#        rect(((width//2)-150), ((height//2)-150), 40, 40,)
        
#Karakter koppel 
    Dio = aap1
    Kakyion = aap2
    Polnareff = aap3
    Jotaro = aap4
    Mrjoestar = aap5

#levensteller
    textSize(30)
    image(hart,1610,50, 100, 100)
    fill(255)
    text(str(currentNumber1), 1650, 100)
    text("DIO", 1350, 100)
    image(hart,1610,150, 100, 100)
    text(str(currentNumber2), 1650, 200)
    text("KAKYOIN", 1350, 200)
    image(hart,1610,250, 100, 100)
    text(str(currentNumber3), 1650, 300)
    text("POLNAREFF", 1350, 300)
    image(hart,1610,350, 100, 100)
    text(str(currentNumber4), 1650, 400)
    text("JOTARO", 1350, 400)
    image(hart,1610,450, 100, 100)
    text(str(currentNumber5), 1650, 500)
    text("MRJOESTAR", 1350, 500)
    e = buttons[15]
    rectFromDict(e)
    f = buttons[16]
    rectFromDict(f)
    g = buttons[17]
    rectFromDict(g)
    textSize(25)
    fill(0)
    text("NEXT", 1770, 650)
    text("PLAYER", 1755, 670)
    
    if dioDead == True:
        textSize(25)
        fill(255,0,0)
        text('DEAD', 1790, 100)
    if kakyoinDead == True:
        textSize(25)
        fill(255,0,0)
        text('DEAD', 1790, 200)
    if polnareffDead == True:
        textSize(25)
        fill(255,0,0)
        text('DEAD', 1790, 300)
    if jotaroDead == True:
        textSize(25)
        fill(255,0,0)
        text('DEAD', 1790, 400)
    if mrjoestarDead == True:
        textSize(25)
        fill(255,0,0)
        text('DEAD', 1790, 500)
    
    if selectedNumber == 0:
        fill(232, 220, 220, 50)
        strokeWeight(4)
        rect(1330, 63, 100, 50, 10)
    if selectedNumber == 1:
        fill(232, 220, 220, 50)
        strokeWeight(4)
        rect(1330, 163, 200, 50, 10)
    if selectedNumber == 2:
        fill(232, 220, 220, 50)
        strokeWeight(4)
        rect(1330, 263, 200, 50, 10)
    if selectedNumber == 3:
        fill(232, 220, 220, 50)
        strokeWeight(4)
        rect(1330, 363, 200, 50, 10)
    if selectedNumber == 4:
        fill(232, 220, 220, 50)
        strokeWeight(4)
        rect(1330, 463, 200, 50, 10)

    
######################################################################### KLIK ONDERDELEN ###########################################################################################################

def mousePressed():
    global TurnTeller, Dobbel, buttons, kakyoinDead, polnareffDead, jotaroDead, mrjoestarDead, dioDead, currentNumber1, currentNumber2, currentNumber3, currentNumber4, currentNumber5, selectedNumber
    
    #Grote dobbel knop
    if checkButton(buttons[8]):
        #Dobbelsteen
        #vakje dobbelstenen
        
        if Dio == True:
            Dobbel = DobbelDio()
        elif Kakyion == True:
            Dobbel = DobbelKakyion()
        elif Polnareff == True:
            Dobbel = DobbelPolnareff()
        elif Jotaro == True:
            Dobbel = DobbelNormaal()
        elif Mrjoestar == True:
            Dobbel = DobbelNormaal()
    
    #Turn systeem
    if checkButton(buttons[9]):
        TurnTeller = TurnTeller + 1
    
    #levensteller
    if selectedNumber == 0:
        if checkButton(buttons[15]):
            if currentNumber1 != 0:
                currentNumber1 -= 1 
        if checkButton(buttons[16]):
            if currentNumber1 != 0:
                currentNumber1 += 1
        if checkButton(buttons[17]):
            selectedNumber = 1
    elif selectedNumber == 1:
        if checkButton(buttons[15]):
            if currentNumber2 != 0:
                currentNumber2 -= 1 
        if checkButton(buttons[16]):
            if currentNumber1 != 0:
                currentNumber2 += 1
        if checkButton(buttons[17]):
            selectedNumber = 2
    elif selectedNumber == 2:
        if checkButton(buttons[15]):
            if currentNumber3 != 0:
                currentNumber3 -= 1 
        if checkButton(buttons[16]):
            if currentNumber1 != 0:
                currentNumber3 += 1
        if checkButton(buttons[17]):
            selectedNumber = 3
    elif selectedNumber == 3:
        if checkButton(buttons[15]):
            if currentNumber4 != 0:
                currentNumber4 -= 1        
        if checkButton(buttons[16]):
            if currentNumber1 != 0:
                currentNumber4 += 1
        if checkButton(buttons[17]):
            selectedNumber = 4
    elif selectedNumber == 4:
        if checkButton(buttons[15]):
            if currentNumber5 != 0:
                currentNumber5 -= 1
        if checkButton(buttons[16]):
            if currentNumber1 != 0:
                currentNumber5 += 1
        if checkButton(buttons[17]):
            selectedNumber = 0
    else:
        selectedNumber = 0
    
    if currentNumber1 == 0:
        dioDead = True
    if currentNumber2 == 0:
        kakyoinDead = True
    if currentNumber3 == 0:
        polnareffDead = True
    if currentNumber4 == 0:
        jotaroDead = True
    if currentNumber5 == 0:
        mrjoestarDead = True

############################################################################# DOBBELSTENEN ##############################################################################################################    
    
def DobbelNormaal():
    global Dobbel_N, DobbelN, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6, Kruis, Dice_To_Draw
    Dobbel_N = [1,2,3,4,5,6]
    DobbelN = random.choice(Dobbel_N)
    if DobbelN == 1:
        Dice_To_Draw = [(Dice_1, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelN == 2:
        Dice_To_Draw = [(Dice_2, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelN == 3:
        Dice_To_Draw = [(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelN == 4:
        Dice_To_Draw = [(Dice_4, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelN == 5:
        Dice_To_Draw = [(Dice_5, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelN == 6:
        Dice_To_Draw = [(Dice_6, ((width//2)-75), ((height//2)-400), 150, 150)]
    
def DobbelDio():
    global Dobbel_D, DobbelD, Dice_To_Draw
    Dobbel_D = [1,2,3,4,5,0]
    DobbelD = random.choice(Dobbel_D)
    if DobbelD == 1:
        Dice_To_Draw = [(Dice_1, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelD == 2:
        Dice_To_Draw = [(Dice_2, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelD == 3:
        Dice_To_Draw = [(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelD == 4:
        Dice_To_Draw = [(Dice_4, ((width//2)-75), ((height//2)-400), 150, 150)]
    elif DobbelD == 5:
        Dice_To_Draw = [(Dice_5, ((width//2)-75), ((height//2)-400), 150, 150)]
    else:
        Dice_To_Draw = [(Kruis, ((width//2)-75), ((height//2)-400), 150, 150)]
    
def DobbelPolnareff():
    global Dobbel_P, DobbelP, Dice_To_Draw
    Dobbel_P = [1,2,3,4,5,6,7,8,9,10,11,12]
    DobbelP = random.choice(Dobbel_P)
    if DobbelP == 1:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 2:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 3:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 4:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 5:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 6:
        Dice_To_Draw = [(Dice_1, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 7:
        Dice_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 8:
        Dic,_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 9:
        Dice_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 10:
        Dice_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 11:
        Dice_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 12:
        Dice_To_Draw = [(Dice_2, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 13:
        Dice_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 14:
        Dic,_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 15:
        Dice_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 116:
        Dice_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 17:
        Dice_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 18:
        Dice_To_Draw = [(Dice_3, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 19:
        Dice_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 20:
        Dic,_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 21:
        Dice_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 22:
        Dice_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 23:
        Dice_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 24:
        Dice_To_Draw = [(Dice_4, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 25:
        Dice_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 26:
        Dic,_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 27:
        Dice_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 28:
        Dice_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 29:
        Dice_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 30:
        Dice_To_Draw = [(Dice_5, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 31:
        Dice_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 32:
        Dic,_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 33:
        Dice_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 34:
        Dice_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 35:
        Dice_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)]
    elif DobbelP == 36:
        Dice_To_Draw = [(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150), (Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)]
    
def DobbelKakyion():
    global Dobbel_K, DobbelK, DobbelK1, Dice_To_Draw
    Dobbel_K = [1,2,3,4]
    DobbelK = random.choice(Dobbel_K)
    if DobbelK == 1:
        Dice_To_Draw = [(Kruis, ((width//2)+122), ((height//2)-375), 125, 125), (Kruis, ((width//2)-8), ((height//2)-375), 125, 125),\
        (Kruis, ((width//2)-137), ((height//2)-375), 125, 125), (Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)]
    elif DobbelK == 2:
        Dice_To_Draw = [(Kruis, ((width//2)+122), ((height//2)-375), 125, 125), (Kruis, ((width//2)-8), ((height//2)-375), 125, 125),\
        (Dice_2, ((width//2)-137), ((height//2)-375), 125, 125), (Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)]
    elif DobbelK == 3:
        Dice_To_Draw = [(Kruis, ((width//2)+122), ((height//2)-375), 125, 125), (Dice_3, ((width//2)-8), ((height//2)-375), 125, 125),\
        (Dice_2, ((width//2)-137), ((height//2)-375), 125, 125), (Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)]
    elif DobbelK == 4:
        Dice_To_Draw= [(Dice_4, ((width//2)+122), ((height//2)-375), 125, 125), (Dice_3, ((width//2)-8), ((height//2)-375), 125, 125),\
        (Dice_2, ((width//2)-137), ((height//2)-375), 125, 125), (Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)]


#levensteller
def selectedNumber():
    global currentNumber1, currentNumber2, currentNumber3, currentNumber4, currentNumber5, buttons
    if selectedNumber == 0:
        selectedNumber = currentNumber1
    if selectedNumber == 1:
        selectedNumber = currentNumber2
    if selectedNumber == 2:
        selectedNumber = currentNumber3
    if selectedNumber == 3:
        selectedNumber = currentNumber4
    if selectedNumber == 4:
        selectedNumber = currentNumber5
############################################################################# DOBBELSTEEN PLAATJES ############################################################################################################
