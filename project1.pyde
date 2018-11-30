def setup():
    global square, isDragging, dragStart
    square = { 'positionX': 15, 'positionY': 15, 'size': 200 } 
    
    isDragging = False
    dragStart = None
    
    size(500,500)
    
def draw():
    clear()
    rect(square['positionX'], square['positionY'], square['size'], square['size'])
    
def mousePressed():
    global isDragging, dragStart
    
    if square['positionX'] < mouseX < square['positionX'] + square['size']:
        if square['positionY'] < mouseY < square['positionY'] + square['size']:
            isDragging = True
            dragStart = (square['positionX'], square['positionY'], mouseX, mouseY)
            
def mouseDragged():
    if isDragging:
        square['positionX'] = dragStart[0] - (dragStart[2] - mouseX)
        square['positionY'] = dragStart[1] - (dragStart[3] - mouseY)
