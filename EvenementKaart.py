import random

def setup():
    global randomlist
    randomlist = ''

def draw():



    fill(100,100,150)
    rect(600, 100, 650, 800)
    fill(255)
    text('Kaart',width/2 - 150, 200)
    fill(100,200,250)
    rect(820, 750, 200, 100)
    fill(255)
    text('Back',830, 825)
    text(randomlist, 700, 500)

def evenementkaart():
    global randomkaart, randomlist

    evenementlist = ['Ga terug naar je respawn punt.', 
                     'Leg een van je kaarten onder aan \nde speelkaarten stapel.', 
                     'Blijf stil staan voor 1 beurt.', 
                     'Je bent geforceerd met de dichtstbijzijnde \nspeler het gevecht aan te gaan.',
                     'Pak 2 kaarten.',
                     'Zet naar keuze 3 extra stappen.',
                     'Kies een een regio waar je naartoe wilt.',
                     # Misschien hier een symbool bij
                     'begin het volgende gevecht met 5 power.',
                     'Ruil een kaart met een speler \nnaar keuzen (willekeurig gekozen)',
                     'Keuze: offer 1 legendary kaart op voor 2 health \nof 1 epic kaart voor 1 health',
                     'Bekijk de bovenste 3 kaarten van de stapel.',
                     'Pak 2 kaarten van onder uit de stapel.',
                     'Als je deze kaart inzet voor een gevecht ontvang je een extra leven.'
                     ]
    randomlist = random.choice(evenementlist)
    
