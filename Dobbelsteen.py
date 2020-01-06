
#Dobbelsteen voor Jotaro en Joseph
def Dobbel_Normaal():
    Gewonedobbel = random.int(1, 6)
    return Gewonedobbel

#Dobbelsteen voor Dio (laat zien bij printen dat er 1 stap af gaat)
def Dobbel_Dio():
    DioDobbel = random.int(0, 5)
    return DioDobbel

#Dobbelsteen voor Kakyoin (bij het printen moet er staan stappenMin t/m stappenMax)
def Dobbel_Kakyoin():
    KakyoinDobbel = random.int(1, 4)
    return KakyoinDobbel

#Dobbelsteen voor Polnaroff (laat zien dat er 3 vanaf gaan)
def Dobbel_Polnaroff():
    PolnaroffDobbel = random.int(1, 12)
    if PolnaroffDobbel <= 3:
        PolnaroffDobbel = 2
    return PolnaroffDobbel


#tijdelijk     
    #Unieke koppel aan karakter spelers
    if aap1 == True:
        Dio = True
        Jotaro = False
        Kakyion = False
        Polnaroff = False
        Mrjoestar = False
    elif aap2 == True:
        Dio = False
        Jotaro = True
        Kakyion = False
        Polnaroff = False
        Mrjoestar = False
    elif aap3 == True:
        Dio = False
        Jotaro = False
        Kakyion = True
        Polnaroff = False
        Mrjoestar = False
    elif aap4 == True:
        Dio = False
        Jotaro = False
        Kakyion = False
        Polnaroff = True
        Mrjoestar = False
    elif aap5 == True:
        Dio = False
        Jotaro = False
        Kakyion = False
        Polnaroff = False
        Mrjoestar = True
    else:
        Dio = False
        Jotaro = False
        Kakyion = False
        Polnaroff = False
        Mrjoestar = False
