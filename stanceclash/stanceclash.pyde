def setup():
    global combinedPower, Hashcode, strHashCode, totalPower, totalPower2, activePlayer, card
    strHashCode = ""
    size(800, 800)
    activePlayer = 0
    totalPower = 0
    totalPower2 = 0
    card = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    #dit is een tekstbox
    #todo alleen zichtbaar wanneer gevraagd
    
    print('Press spacebar to initiate the battle')
    
    #minion1 = card[0]
    #minion2 = card[1]

    #print(card[0])
    #print(card[1])
    
    #combinedPower = card['1'] + card['2']
    
    #print('Adding the power level of minion 1: ' + str(card['1']) + ' to the power level of minion 2: ' + str(card['2']) + ' will give a total power level of: ' + str(combinedPower))
    
def draw():
    global strHashCode
    background(0)
    fill(100, 150, 230)
    rect(200, 200, 400, 200)
    fill(255)
    text(strHashCode, 200, 200)
    
    
def keyPressed():
    global hashCode, strHashCode, totalPower, totalPower2, activePlayer
    
    if 49 <= keyCode <= 57 or 97 <= keyCode <= 105:
        hashCode = int(key)
        strHashCode += key
    
    #activeplayer += 1
    
    #print('we are here 1')
    
    #print(key)
    #print(type(key))
    
    
    #print(keyCode)
    if keyCode == 40:
        activePlayer += 1
    #CHECK OF HET NIET GROTER IS DAN HET MAXIMALE AANTAL SPELERS EN NIET KLEINER IS DAN 0
    if keyCode == 38:
        activePlayer -= 1
    
    
    if keyCode == 32:
        print('Player 1 his/her turn has started')
        activePlayer = 1
        print('Please enter a card hashcode between 1 and 29')
        
    if keyCode  == 10 and activePlayer == 1:
        if int(strHashCode) > len(card):
            strHashCode = ''
            print("voer een getal tussen 1 en 30 in")
            hashCode = key
        else:
            print('The power of your selected card is:'),
            print(card[int(strHashCode)])
            totalPower += card[int(strHashCode)]
            strHashCode = ''
            print('The total power of player 1 is:'),
            print(totalPower)
            
    if activePlayer == 2:
        print('Player 2 his/her turn has started')
        print('Please enter a card hashcode between 1 and 29')
        if key == ENTER:
            if int(strHashCode) > len(card):
                strHashCode = ''
                print("voer een getal tussen 1 en 30 in")
                hashCode = key
            else:
                print('The power of your selected card is:'),
                print(card[int(strHashCode)])
                totalPower2 += card[int(strHashCode)]
                strHashCode = ''
                print('The total power of player 2 is:'),
                print(totalPower2) 
                

    

           
    
    
    
        
    
