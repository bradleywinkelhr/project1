import random

newRandom = random.randint
def setup():
    # Make sure that variables are accesible everywhere
    global square, randomNmr, elipse
    # Create a square
    square = { 'positionX': 150, 'positionY': 150, 'size': 200 }
    elipse = { 'positionX': 125, 'positionY': 125, 'size': 200 }
    # Change the size of the screen
    size(500, 500)
    
def draw():
    # Draw the square
    rect(square['positionX'], square['positionY'], square['size'], square['size'])
    randomNmr = newRandom(1,6)
    
    if square['positionX'] < mouseX < square['positionX'] + square['size']:
    # Check whether the Y's collide
        if square['positionY'] < mouseY < square['positionY'] + square['size']:
            if mousePressed == True:
                if (randomNmr == 1 or randomNmr == 3 or randomNmr == 5):
                    ellipse(width/2, height/2, elipse['size']/5,  elipse['size']/5) 
                if (randomNmr == 2 or randomNmr == 3 or randomNmr == 4 or randomNmr == 5 or randomNmr == 6): 
                    ellipse(width/2 -  elipse['size']/4, height/2 -  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
                    ellipse(width/2 +  elipse['size']/4, height/2 +  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
                if (randomNmr == 4 or randomNmr == 5 or randomNmr == 6): 
                    ellipse(width/2 -  elipse['size']/4, height/2 +  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
                    ellipse(width/2 +  elipse['size']/4, height/2 -  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
                if (randomNmr == 6):
                    ellipse(width/2, height/2 -  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
                    ellipse(width/2, height/2 +  elipse['size']/4,  elipse['size']/5,  elipse['size']/5)
    
def mouseReleased():
    # Check whether the X's collide
    clear()
