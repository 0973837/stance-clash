
def setup():
    global DioLevens, DioDead, Hartjeimg
    size(1920, 1080)
    DioLevens = 3
    DioDead = False
    Hartjeimg = loadImage("hartje.png")

def draw():
    global DioLevens, DioDead, Hartjeimg
    background(225)
    
    #De '-' (rode)knop V
    fill(255,0,0)
    rect(400,100, 50, 50)
    #De '-'
    fill(0)
    rect(412.5, 122.5, 25, 5)
    
    #De '+' (groene)knop V
    fill(0,255,0)
    rect(475, 100, 50, 50)
    #De '+'
    fill(0)
    rect(487.5, 122.5 , 25, 5)
    rect(497.5, 112.5 , 5, 25)
    
    #Het Hartje
    image(Hartjeimg, 321,98)
    #Het aantal levens:
    textSize(40)
    text(str(DioLevens), 340,140)
    
    if DioDead == True:
        fill(255,0,0)
        text('Dio has died!', 600, 140)
    
def mousePressed():
    global DioLevens, DioDead
    #Button functie '-'
    if mouseX > 400 and mouseX < 450 and mouseY > 100 and mouseY < 150:
        if DioLevens > 0:
            DioLevens = DioLevens - 1
            print(DioLevens)
        if DioLevens == 0:
            DioDead = True
    if mouseX > 475 and mouseX < 525 and mouseY > 100 and mouseY < 150:
        DioLevens = DioLevens + 1
        print(DioLevens)
    

    
    
    
    
    
    
