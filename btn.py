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
    "textColor": color(232, 220, 220, 200)
}

spelersBackButton = {
    "x":900,
    "y": 600,
    "width": 150,
    "height": 100,
    "text": "BACK",
    "textHeight": 65,
    "textWidth": 10,
    "textColor": color(5,5,5)
}

jotaroScherm = {
    "x":150,
    "y": 100,
    "width": 150,
    "height": 100,
    "textHeight": 0,
    "textWidth": 0,
}

dioScherm = {
    "x":550,
    "y": 100,
    "width": 150,
    "height": 100,
    "textHeight": 0,
    "textWidth": 0,
}

polnareffScherm = {
    "x":950,
    "y": 100,
    "width": 150,
    "height": 100,
    "textHeight": 0,
    "textWidth": 0,
}

kokyoinScherm = {
    "x":350,
    "y": 300,
    "width": 150,
    "height": 100,
    "textHeight": 0,
    "textWidth": 0,
}

mrjoestarScherm = {
    "x":750,
    "y": 300,
    "width": 150,
    "height": 100,
    "textHeight": 0,
    "textWidth": 0,
}



buttons.append(startSchermButton)
buttons.append(spelersBackButton)
buttons.append(jotaroScherm)
buttons.append(dioScherm)
buttons.append(polnareffScherm)
buttons.append(kokyoinScherm)
buttons.append(mrjoestarScherm)



def rectFromDict(d):
    rect(d["x"],d["y"], d["width"], d["height"])
    fill(d["textColor"])
    text(d["text"], d["x"]+ d["textWidth"] ,d["y"] + d["textHeight"])

def checkButton(d):
    if d["x"] <= mouseX and mouseX <= d["x"]+ d["width"] and d["y"]<= mouseY and mouseY <= d["y"] + d["height"]:
        return True
    else:
        return False
