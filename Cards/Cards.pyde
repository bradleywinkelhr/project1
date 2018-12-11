import random

# Create variables for the position of the star
cardX = 0
cardY = 0
rng = random.randint(1,10)

def setup():
    # Create a local variable for photo
    global cardS
    
    # Change the size of the screen
    size(250, 250)
    
    # Load the card image
    for i in range (0,50):
        if i == rng:
            cardS = loadImage("kaart" + str(i) + ".png")

    
def draw():
    # Make sure that we can edit the global variables
    global cardX, cardY
    
    # Clear the screen
    clear()

    # Draw the star
    image(cardS, cardX, cardY, 250, 250)
    
