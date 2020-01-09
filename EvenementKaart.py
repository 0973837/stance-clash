import random
from btn import *


def setup():
    global randomlist, scherm
    randomlist = ''
    scherm = 10

def draw():
    global buttons
    
    textSize(40)
    x = buttons[1]
    rectFromDict(x)
    textSize(75)
    y = buttons[14]
    rectFromDict(y)
    textSize(40)
    text(randomlist, 620, 400, 600, 600)

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
