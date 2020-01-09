WIDTH = 1920
HEIGHT = 1080
buttons = []

startSchermButton = {
    "x":WIDTH /2 - 80,
    "y": HEIGHT/ 2 + 40,
    "width": 200,
    "height": 100,
    "text": "START",
    "textHeight": 70,
    "textWidth": 20,
    "textColor": color(232, 220, 220, 200),
    "buttonBackgroundColor": color(232, 220, 220, 50),
}

spelersBackButton = {
    "x":200,
    "y": 800,
    "width": 150,
    "height": 100,
    "text": "BACK",
    "textHeight": 65,
    "textWidth": 20,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

spelersNextButton = {
    "x":1600,
    "y": 800,
    "width": 150,
    "height": 100,
    "text": "NEXT",
    "textHeight": 65,
    "textWidth": 20,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}


jotaroScherm = {
    "x":150,
    "y": 100,
    "width": 250,
    "height": 200,
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

dioScherm = {
    "x":825,
    "y": 100,
    "width": 250,
    "height": 200,
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

polnareffScherm = {
    "x":1450,
    "y": 100,
    "width": 250,
    "height": 200,
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

kokyoinScherm = {
    "x":500,
    "y": 400,
    "width": 250,
    "height": 200,
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

mrjoestarScherm = {
    "x":1150,
    "y": 400,
    "width": 250,
    "height": 200,
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

dobbelknopButton = {
    "x":WIDTH//2-150,
    "y": HEIGHT//2-150,
    "width": 300,
    "height": 300,
    "text": "",
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

turnsysteemButton = {
    "x":400,
    "y": 50,
    "width": 50,
    "height": 50,
    "text": "",
    "textHeight": 0,
    "textWidth": 0,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

evenementButton = {
    "x":1600,
    "y": 800,
    "width": 250,
    "height": 100,
    "text": "EVENEMENT",
    "textHeight": 65,
    "textWidth": 10,
    "textColor": color(5,5,5),
    "buttonBackgroundColor": color(255),
}

eventButton = {
    "x": WIDTH/2 - 200,
    "y": HEIGHT / 2 + 40,
    "width": 300,
    "height": 100,
    "text": "EVENT",
    "textHeight": 65,
    "textWidth": 20,
    "textColor": color(150,200,255),
    "buttonBackgroundColor": color(225),
}

startEventButton = {
    "x": WIDTH/2 - 200,
    "y": HEIGHT / 2 - 100,
    "width": 300,
    "height": 100,
    "text": "START EVENT",
    "textHeight": 65,
    "textWidth": 20,
    "textColor": color(170),
    "buttonBackgroundColor": color(150,200,225),
}

kaartBackButton = {
    "x": 820,
    "y": 750,
    "width": 200,
    "height": 100,
    "text": "BACK",
    "textHeight": 65,
    "textWidth": 20,
    "textColor": color(255),
    "buttonBackgroundColor": color(100,200,250),
}

kaartButton = {
    "x": 600,
    "y": 100,
    "width": 650,
    "height": 800,
    "text": "KAART",
    "textHeight": 80,
    "textWidth": 200,
    "textColor": color(255),
    "buttonBackgroundColor": color(100,100,150),
}

minButton = {
    "x":1450,
    "y": 600,
    "width": 100,
    "height": 100,
    "text": "-",
    "textHeight": 60,
    "textWidth": 40,
    "textColor": color(255,9,0),
    "buttonBackgroundColor": color(255),
}

plusButton = {
    "x":1600,
    "y": 600,
    "width": 100,
    "height": 100,
    "text": "+",
    "textHeight": 60,
    "textWidth": 40,
    "textColor": color(16,255,0),
    "buttonBackgroundColor": color(255),
}

nextPlayerButton = {
    "x":1750,
    "y": 600,
    "width": 100,
    "height": 100,
    "text": "",
    "textHeight": 50,
    "textWidth": 15,
    "textColor": color(0),
    "buttonBackgroundColor": color(255),
}


buttons.append(startSchermButton)
buttons.append(spelersBackButton)
buttons.append(jotaroScherm)
buttons.append(dioScherm)
buttons.append(polnareffScherm)
buttons.append(kokyoinScherm)
buttons.append(mrjoestarScherm)
buttons.append(spelersNextButton)
buttons.append(dobbelknopButton)
buttons.append(turnsysteemButton)
buttons.append(evenementButton)
buttons.append(eventButton)
buttons.append(startEventButton)
buttons.append(kaartBackButton)
buttons.append(kaartButton)
buttons.append(minButton)
buttons.append(plusButton)
buttons.append(nextPlayerButton)



def rectFromDict(d):
    fill(d["buttonBackgroundColor"])
    rect(d["x"],d["y"], d["width"], d["height"])
    fill(d["textColor"])
    text(d["text"], d["x"]+ d["textWidth"] ,d["y"] + d["textHeight"])

def checkButton(d):
    if d["x"] <= mouseX and mouseX <= d["x"]+ d["width"] and d["y"]<= mouseY and mouseY <= d["y"] + d["height"]:
        return True
    else:
        return False
