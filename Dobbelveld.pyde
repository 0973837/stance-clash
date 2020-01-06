import random

#MainScreen
def setup():
    global tijd, DobbelsteenImg, aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel_N, DobbelN, Dobbel_D, DobbelD, Dobbel_P, DobbelP, Dobbel_K, DobbelK, DobbelK1, Dobbel, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6                                         
    fullScreen()
    
#Variables
    DobbelsteenImg = loadImage("Dice.png")
    
    TurnTeller = 0
    
    Background = loadImage("Jojo turn background.png")
    
    Dice_6 = loadImage("Dice #6.png")
    Dice_5 = loadImage("Dice #5.png")
    Dice_4 = loadImage("Dice #4.png")
    Dice_3 = loadImage("Dice #3.png")
    Dice_2 = loadImage("Dice #2.png")
    Dice_1 = loadImage("Dice #1.png")
    
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
    
    
def draw():
    global DobbelsteenImg,  aap1, aap2, aap3, aap4, aap5, TurnTeller, Background, Dio, Jotaro, Polnareff, Kakyion, Mrjoestar, Dobbel
    
################################################################################################ DOBBEL ONDERDEEL ########################################################################################################################
    
#De dobbel knop
    noFill()
    rect(((width//2)-150), ((height//2)-150), 300, 300,)
    
#Afbeelding in de dobbel knop
    image(DobbelsteenImg, ((width//2)-135), ((height//2)-135))
    
    
################################################################################################# TURN ONDERDEEL ##########################################################################################################################
    
#Turn veld
    fill(250)
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
        text("aap 1", 150, 90)
        text("aap 2", 75, 150)
        text("aap 3", 75, 210)
        text("aap 4", 75, 270)
        text("aap 5", 75, 330)
    elif aap2 == True:
        text("aap 1", 75, 90)
        text("aap 2", 150, 150)
        text("aap 3", 75, 210)
        text("aap 4", 75, 270)
        text("aap 5", 75, 330)
    elif aap3 == True:
        text("aap 1", 75, 90)
        text("aap 2", 75, 150)
        text("aap 3", 150, 210)
        text("aap 4", 75, 270)
        text("aap 5", 75, 330)
    elif aap4 == True:
        text("aap 1", 75, 90)
        text("aap 2", 75, 150)
        text("aap 3", 75, 210)
        text("aap 4", 150, 270)
        text("aap 5", 75, 330)
    elif aap5 == True:
        text("aap 1", 75, 90)
        text("aap 2", 75, 150)
        text("aap 3", 75, 210)
        text("aap 4", 75, 270)
        text("aap 5", 150, 330)
    else:
        text("aap 1", 75, 90)
        text("aap 2", 75, 150)
        text("aap 3", 75, 210)
        text("aap 4", 75, 270)
        text("aap 5", 75, 330)
        
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
    if Dio == True:
        fill(50)
        rect(((width//2)-150), ((height//2)-150), 40, 40,)
    elif Kakyion == True:
        fill(100)
        rect(((width//2)-150), ((height//2)-150), 40, 40,)
    elif Polnareff == True:
        fill(150)
        rect(((width//2)-150), ((height//2)-150), 40, 40,)
    elif Jotaro == True:
        fill(200)
        rect(((width//2)-150), ((height//2)-150), 40, 40,)
    elif Mrjoestar == True:
        fill(250)
        rect(((width//2)-150), ((height//2)-150), 40, 40,)
        
#Karakter koppel 
    Dio = aap1
    Kakyion = aap2
    Polnareff = aap3
    Jotaro = aap4
    Mrjoestar = aap5
    
######################################################################### ACHTERGROND ############################################################################################################
    
#Background
    #background(Background)
    
    
######################################################################### KLIK ONDERDELEN ###########################################################################################################

def mousePressed():
    global TurnTeller, Dobbel
    
    #Grote dobbel knop
    if mouseX > ((width//2)-150) and mouseX < ((width//2)+150) and mouseY > ((height//2)-150) and mouseY < ((height//2)+150):
        #Dobbelsteen
        
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
    global Dobbel_N, DobbelN, Dice_1, Dice_2, Dice_3, Dice_4, Dice_5, Dice_6
    Dobbel_N = [1,2,3,4,5,6]
    DobbelN = random.choice(Dobbel_N)
    if DobbelN == 1:
        image(Dice_1, ((width//2)-135), ((height//2)-135))
    elif DobbelN == 2:
        image(Dice_2, ((width//2)-135), ((height//2)-135))
    elif DobbelN == 3:
        image(Dice_3, ((width//2)-135), ((height//2)-135))
    elif DobbelN == 4:
        image(Dice_4, ((width//2)-135), ((height//2)-135))
    elif DobbelN == 5:
        image(Dice_5, ((width//2)-135), ((height//2)-135))
    elif DobbelN == 6:
        image(Dice_6, ((width//2)-135), ((height//2)-135))
    
def DobbelDio():
    global Dobbel_D, DobbelD
    Dobbel_D = [1,2,3,4,5,0]
    DobbelD = random.choice(Dobbel_D)
    print(DobbelD)
    
def DobbelPolnareff():
    global Dobbel_P, DobbelP
    
    Dobbel_P = [1,2,3,4,5,6,7,8,9,10,11,12]
    DobbelP = random.choice(Dobbel_P)
    if DobbelP <= 3:
        DobbelP = 2
    print(DobbelP)
    
def DobbelKakyion():
    global Dobbel_K, DobbelK, DobbelK1
    
    Dobbel_K = [1,2,3,4]
    DobbelK = random.choice(Dobbel_K)
    DobbelK1 = 1
    while DobbelK1 <= DobbelK:
        print(DobbelK1)
        DobbelK1 = DobbelK1 + 1
        
############################################################################# DOBBELSTEEN PLAATJES ############################################################################################################
