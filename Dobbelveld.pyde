import random

#MainScreen
def setup():
    global DobbelsteenImg, Menacing, aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel_N, DobbelN, Dobbel_D, DobbelD, Dobbel_P, DobbelP, Dobbel_K, DobbelK, DobbelK1, Dobbel, Kruis, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6                                         
    fullScreen()
    
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
    
    background(Background)
    
    
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
    
#vakje dobbelstenen
    fill(255)
    stroke(3)
    rect(((width//2)-270), ((height//2)-410), 520, 170)
    
    
def draw():
    global DobbelsteenImg,  aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel, Menacing
    
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
        
#End turn knop
    fill(255)
    rect(400, 50, 50, 50)
    
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
    
######################################################################### KLIK ONDERDELEN ###########################################################################################################

def mousePressed():
    global TurnTeller, Dobbel
    
    #Grote dobbel knop
    if mouseX > ((width//2)-150) and mouseX < ((width//2)+150) and mouseY > ((height//2)-150) and mouseY < ((height//2)+150):
        #Dobbelsteen
        #vakje dobbelstenen
        fill(255)
        stroke(3)
        rect(((width//2)-270), ((height//2)-410), 520, 170)
        
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
        print(Dobbel)
    
    #Turn systeem
    if mouseX > 400 and mouseX < 450 and mouseY > 50 and mouseY < 100:
        TurnTeller = TurnTeller + 1

############################################################################# DOBBELSTENEN ##############################################################################################################    
    
def DobbelNormaal():
    global Dobbel_N, DobbelN, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6, Kruis
    Dobbel_N = [1,2,3,4,5,6]
    DobbelN = random.choice(Dobbel_N)
    if DobbelN == 1:
        image(Dice_1, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelN == 2:
        image(Dice_2, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelN == 3:
        image(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelN == 4:
        image(Dice_4, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelN == 5:
        image(Dice_5, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelN == 6:
        image(Dice_6, ((width//2)-75), ((height//2)-400), 150, 150)
    
def DobbelDio():
    global Dobbel_D, DobbelD
    Dobbel_D = [1,2,3,4,5,0]
    DobbelD = random.choice(Dobbel_D)
    if DobbelD == 1:
        image(Dice_1, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelD == 2:
        image(Dice_2, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelD == 3:
        image(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelD == 4:
        image(Dice_4, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelD == 5:
        image(Dice_5, ((width//2)-75), ((height//2)-400), 150, 150)
    else:
        image(Kruis, ((width//2)-75), ((height//2)-400), 150, 150)
    
def DobbelPolnareff():
    global Dobbel_P, DobbelP
    Dobbel_P = [1,2,3,4,5,6,7,8,9,10,11,12]
    DobbelP = random.choice(Dobbel_P)
    if DobbelP == 1:
        image(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 2:
        image(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 3:
        image(Dice_3, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 4:
        image(Dice_4, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 5:
        image(Dice_5, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 6:
        image(Dice_6, ((width//2)-75), ((height//2)-400), 150, 150)
    elif DobbelP == 7:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_1, ((width//2)-155), ((height//2)-400), 150, 150)
    elif DobbelP == 8:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_2, ((width//2)-155), ((height//2)-400), 150, 150)
    elif DobbelP == 9:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_3, ((width//2)-155), ((height//2)-400), 150, 150)
    elif DobbelP == 10:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_4, ((width//2)-155), ((height//2)-400), 150, 150)
    elif DobbelP == 11:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_5, ((width//2)-155), ((height//2)-400), 150, 150)
    elif DobbelP == 12:
        image(Dice_6, ((width//2)+5), ((height//2)-400), 150, 150)
        image(Dice_6, ((width//2)-155), ((height//2)-400), 150, 150)
    
def DobbelKakyion():
    global Dobbel_K, DobbelK, DobbelK1
    Dobbel_K = [1,2,3,4]
    DobbelK = random.choice(Dobbel_K)
    if DobbelK == 1:
        image(Kruis, ((width//2)+122), ((height//2)-375), 125, 125)
        image(Kruis, ((width//2)-8), ((height//2)-375), 125, 125)
        image(Kruis, ((width//2)-137), ((height//2)-375), 125, 125)
        image(Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)
    elif DobbelK == 2:
        image(Kruis, ((width//2)+122), ((height//2)-375), 125, 125)
        image(Kruis, ((width//2)-8), ((height//2)-375), 125, 125)
        image(Dice_2, ((width//2)-137), ((height//2)-375), 125, 125)
        image(Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)
    elif DobbelK == 3:
        image(Kruis, ((width//2)+122), ((height//2)-375), 125, 125)
        image(Dice_3, ((width//2)-8), ((height//2)-375), 125, 125)
        image(Dice_2, ((width//2)-137), ((height//2)-375), 125, 125)
        image(Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)
    elif DobbelK == 4:
        image(Dice_4, ((width//2)+122), ((height//2)-375), 125, 125)
        image(Dice_3, ((width//2)-8), ((height//2)-375), 125, 125)
        image(Dice_2, ((width//2)-137), ((height//2)-375), 125, 125)
        image(Dice_1, ((width//2)-263), ((height//2)-375), 125, 125)
        
############################################################################# DOBBELSTEEN PLAATJES ############################################################################################################
