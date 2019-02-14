# space scrambles the Cube randomly
# r, u, b, etc, move the Cube in there respective ways
# holding shift will do the counter clockwise move


# SETUP! defs, imports, and initiation
import random

numSides = 3 # the number of sides 
blockSize = 240 / numSides # the size of one piece
blockColorSize = blockSize * .75 # the size of the color in proportion
viewState = 'locked' # for the toggleable camera
x = numSides # these are equal to 3
y = numSides


class Block(object): # block

# if there is a None, it means that color doesnt exist
    def __init__(self, name, type, xFace, yFace, zFace):
        self.name = name
        self.type = type
        self.xFace = xFace
        self.yFace = yFace
        self.zFace = zFace
        
        
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************


# this section is for the actual visual cube  

# creating the blocks, set up in the same format as Cube 
white_orange_green =     Block('white_orange_green',           'corner',   'green',   'orange',   'white')
orange_green =           Block('orange_green',                 'edge',     'green',   'orange',   None)
yellow_orange_green =    Block('yellow_orange_green',          'corner',   'green',   'orange',   'yellow')
    
white_green =            Block('white_green',                  'edge',     'green',   None,       'white')
green_ =                 Block('green',                       'center',   'green',   None,       None)
yellow_green =           Block('yellow_green',                 'edge',     'green',   None,       'yellow')
    
white_red_green =        Block('white_red_green',              'corner',   'green',   'red',      'white')
red_green =              Block('red_green',                    'edge',     'green',   'red',      None)
yellow_red_green =       Block('yellow_red_green',             'corner',   'green',   'red',      'yellow')
    
    
white_orange =           Block('white_orange',                 'edge',     None,      'orange',   'white')
orange_ =                Block('orange',                      'center',   None,      'orange',   None)
yellow_orange =          Block('yellow_orange',                'edge',     None,      'orange',   'yellow')
    
white_ =                 Block('white',                       'center',   None,      None,       'white')
core =                   Block('core',                         'core',     None,      None,       None)
yellow_ =                Block('yellow',                      'center',   None,      None,       'yellow')
    
white_red =              Block('white_red',                    'edge',     None,      'red',      'white')
red_ =                   Block('red',                         'center',   None,      'red',      None)
yellow_red =             Block('yellow_red',                   'edge',     None,      'red',      'yellow')
    
    
white_orange_blue =      Block('white_orange_blue',            'corner',   'blue',    'orange',   'white')
orange_blue =            Block('orange_blue',                  'edge',     'blue',    'orange',   None)
yellow_orange_blue =     Block('yellow_orange_blue',           'corner',   'blue',    'orange',   'yellow')
    
white_blue =             Block('white_blue',                   'edge',     'blue',    None,       'white')
blue_ =                  Block('blue',                        'center',   'blue',    None,       None)
yellow_blue =            Block('yellow_blue',                  'edge',     'blue',    None,       'yellow')
    
white_red_blue =         Block('white_red_blue',               'corner',   'blue',    'red',      'white')
red_blue =               Block('red_blue',                     'edge',     'blue',    'red',      None)
yellow_red_blue =        Block('yellow_red_blue',              'corner',   'blue',    'red',      'yellow')
    
    
    
    
    # Cube array
Cube = [# this is the actual setup for the Cube, and can be used to figure out what is where
                  # can be referanced by x, y, z
                  # 0, 0, 0 is the left, front, bottom
                
[[ white_orange_green, orange_green, yellow_orange_green ], 
[ white_green, green_, yellow_green ],
[ white_red_green, red_green, yellow_red_green ]],
    
[[ white_orange, orange_, yellow_orange ], 
[ white_, core, yellow_ ],
[ white_red, red_, yellow_red ]],
    
[[ white_orange_blue, orange_blue, yellow_orange_blue ], 
[ white_blue, blue_, yellow_blue ],
[ white_red_blue, red_blue, yellow_red_blue ]]]

# this is a 3d list that takes the faces of each side so that the Cube visualation is integrated

block = [ #### if you change this list change the one in refreshBlock(Cube) ####
    [ # orange
    [Cube[2][0][0].yFace, Cube[2][0][1].yFace, Cube[2][0][2].yFace],
    [Cube[1][0][0].yFace, Cube[1][0][1].yFace, Cube[1][0][2].yFace],
    [Cube[0][0][0].yFace, Cube[0][0][1].yFace, Cube[0][0][2].yFace]
    ],
    [ # green
    [Cube[0][0][0].xFace, Cube[0][0][1].xFace, Cube[0][0][2].xFace],
    [Cube[0][1][0].xFace, Cube[0][1][1].xFace, Cube[0][1][2].xFace],
    [Cube[0][2][0].xFace, Cube[0][2][1].xFace, Cube[0][2][2].xFace]
    ],   
    [ # yellow
    [Cube[2][0][2].zFace, Cube[2][1][2].zFace, Cube[2][2][2].zFace],
    [Cube[1][0][2].zFace, Cube[1][1][2].zFace, Cube[1][2][2].zFace],
    [Cube[0][0][2].zFace, Cube[0][1][2].zFace, Cube[0][2][2].zFace]
    ],    
    [ # red
    [Cube[0][2][0].yFace, Cube[0][2][1].yFace, Cube[0][2][2].yFace],
    [Cube[1][2][0].yFace, Cube[1][2][1].yFace, Cube[1][2][2].yFace],
    [Cube[2][2][0].yFace, Cube[2][2][1].yFace, Cube[2][2][2].yFace]
    ],
    [ # blue
    [Cube[2][2][0].xFace, Cube[2][2][1].xFace, Cube[2][2][2].xFace],
    [Cube[2][1][0].xFace, Cube[2][1][1].xFace, Cube[2][1][2].xFace],
    [Cube[2][0][0].xFace, Cube[2][0][1].xFace, Cube[2][0][2].xFace]
    ],
    [ # white
    [Cube[2][2][0].zFace, Cube[2][1][0].zFace, Cube[2][0][0].zFace],
    [Cube[1][2][0].zFace, Cube[1][1][0].zFace, Cube[1][0][0].zFace],
    [Cube[0][2][0].zFace, Cube[0][1][0].zFace, Cube[0][0][0].zFace]
    ]]
 
 
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    
    
# this section deals with the solved cube    
    
s_white_orange_green =     Block('white_orange_green',           'corner',   'green',   'orange',   'white')
s_orange_green =           Block('orange_green',                 'edge',     'green',   'orange',   None)
s_yellow_orange_green =    Block('yellow_orange_green',          'corner',   'green',   'orange',   'yellow')
s_white_green =            Block('white_green',                  'edge',     'green',   None,       'white')
s_green_ =                 Block('green',                       'center',   'green',   None,       None)
s_yellow_green =           Block('yellow_green',                 'edge',     'green',   None,       'yellow')
s_white_red_green =        Block('white_red_green',              'corner',   'green',   'red',      'white')
s_red_green =              Block('red_green',                    'edge',     'green',   'red',      None)
s_yellow_red_green =       Block('yellow_red_green',             'corner',   'green',   'red',      'yellow')
s_white_orange =           Block('white_orange',                 'edge',     None,      'orange',   'white')
s_orange_ =                Block('orange',                      'center',   None,      'orange',   None)
s_yellow_orange =          Block('yellow_orange',                'edge',     None,      'orange',   'yellow')
s_white_ =                 Block('white',                       'center',   None,      None,       'white')
s_core =                   Block('core',                         'core',     None,      None,       None)
s_yellow_ =                Block('yellow',                      'center',   None,      None,       'yellow')
s_white_red =              Block('white_red',                    'edge',     None,      'red',      'white')
s_red_ =                   Block('red',                         'center',   None,      'red',      None)
s_yellow_red =             Block('yellow_red',                   'edge',     None,      'red',      'yellow')
s_white_orange_blue =      Block('white_orange_blue',            'corner',   'blue',    'orange',   'white')
s_orange_blue =            Block('orange_blue',                  'edge',     'blue',    'orange',   None)
s_yellow_orange_blue =     Block('yellow_orange_blue',           'corner',   'blue',    'orange',   'yellow')
s_white_blue =             Block('white_blue',                   'edge',     'blue',    None,       'white')
s_blue_ =                  Block('blue',                        'center',   'blue',    None,       None)
s_yellow_blue =            Block('yellow_blue',                  'edge',     'blue',    None,       'yellow')
s_white_red_blue =         Block('white_red_blue',               'corner',   'blue',    'red',      'white')
s_red_blue =               Block('red_blue',                     'edge',     'blue',    'red',      None)
s_yellow_red_blue =        Block('yellow_red_blue',              'corner',   'blue',    'red',      'yellow')
        
SolvedCube = [[[ s_white_orange_green, s_orange_green, s_yellow_orange_green ], 
[ s_white_green, s_green_, s_yellow_green ],
[ s_white_red_green, s_red_green, s_yellow_red_green ]],
[[ s_white_orange, s_orange_, s_yellow_orange ], 
[ s_white_, s_core, s_yellow_ ],
[ s_white_red, s_red_, s_yellow_red ]],
[[ s_white_orange_blue, s_orange_blue, s_yellow_orange_blue ], 
[ s_white_blue, s_blue_, s_yellow_blue ],
[ s_white_red_blue, s_red_blue, s_yellow_red_blue ]]]          
    
SolvedBlock = [[[SolvedCube[2][0][0].yFace, SolvedCube[2][0][1].yFace, SolvedCube[2][0][2].yFace],
[SolvedCube[1][0][0].yFace, SolvedCube[1][0][1].yFace, SolvedCube[1][0][2].yFace],
[SolvedCube[0][0][0].yFace, SolvedCube[0][0][1].yFace, SolvedCube[0][0][2].yFace]],
[[SolvedCube[0][0][0].xFace, SolvedCube[0][0][1].xFace, SolvedCube[0][0][2].xFace],
[SolvedCube[0][1][0].xFace, SolvedCube[0][1][1].xFace, SolvedCube[0][1][2].xFace],
[SolvedCube[0][2][0].xFace, SolvedCube[0][2][1].xFace, SolvedCube[0][2][2].xFace]],   
[[SolvedCube[2][0][2].zFace, SolvedCube[2][1][2].zFace, SolvedCube[2][2][2].zFace],
[SolvedCube[1][0][2].zFace, SolvedCube[1][1][2].zFace, SolvedCube[1][2][2].zFace],
[SolvedCube[0][0][2].zFace, SolvedCube[0][1][2].zFace, SolvedCube[0][2][2].zFace]],    
[[SolvedCube[0][2][0].yFace, SolvedCube[0][2][1].yFace, SolvedCube[0][2][2].yFace],
[SolvedCube[1][2][0].yFace, SolvedCube[1][2][1].yFace, SolvedCube[1][2][2].yFace],
[SolvedCube[2][2][0].yFace, SolvedCube[2][2][1].yFace, SolvedCube[2][2][2].yFace]],
[[SolvedCube[2][2][0].xFace, SolvedCube[2][2][1].xFace, SolvedCube[2][2][2].xFace],
[SolvedCube[2][1][0].xFace, SolvedCube[2][1][1].xFace, SolvedCube[2][1][2].xFace],
[SolvedCube[2][0][0].xFace, SolvedCube[2][0][1].xFace, SolvedCube[2][0][2].xFace]],
[[SolvedCube[2][2][0].zFace, SolvedCube[2][1][0].zFace, SolvedCube[2][0][0].zFace],
[SolvedCube[1][2][0].zFace, SolvedCube[1][1][0].zFace, SolvedCube[1][0][0].zFace],
[SolvedCube[0][2][0].zFace, SolvedCube[0][1][0].zFace, SolvedCube[0][0][0].zFace]]]

    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************


# this section is the actual running code the does various things like generate the cube or set it up
    
def setup(): # this only runs once
    
    size(600, 600, P3D) # creates window in 3d mode 
    strokeWeight(5)
    noFill()
    rectMode(CENTER)

    
# *************************************************************************************************


def draw():
    background(100, 100, 150) # background color
    translate(width / 2, height / 2) # moves the Cube so its actually in the frame
    fill(255)
    
    if viewState == 'free': # becasue of the way camera stuff works, this needs to be in draw
        rotateX(-mouseY * PI / 300)    # when you click the mouse, a function changes the variable viewState
        rotateY(-mouseX * PI / 300)     # this top code follows mouse
    else:
        rotateX((3 * PI / 4) + (PI / 16)) # the Cube is set to a default position, which is + PI / 16 off normal
        rotateY((5 * PI / 4) - (PI / 16))

    createCubeVisual()
    
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    
    
# this section is various function defs
    
def createCubeVisual():        
    global Cube
    global block
    refreshBlock() # updates the block array to the correct config
    
    for face in range(0, 6): # runs through the colors
        for x in range(0, 3): # creates a triple nested loop, the outside 2 loops run 3 times, the inside one runs 6 times
            for y in range(0, 3): # they run through and create all of the colors needed at the correct positionsr
                if face == 0: # orange
                    pushMatrix() # retrives a default pos
                    # no rotation
                    colorFaces(face, x, y) # this draw the face we are on, in this case its orange
                    popMatrix() # undos the default pos
                if face == 1: # green
                    pushMatrix()
                    rotateY(PI / 2)
                    colorFaces(face, x, y)
                    popMatrix()
                if face == 2: # yellow
                    pushMatrix()
                    rotateX(-PI / 2)
                    colorFaces(face, x, y)
                    popMatrix()
                if face == 3: # red
                    pushMatrix()
                    rotateY(PI)
                    colorFaces(face, x, y)
                    popMatrix()
                if face == 4: # blue
                    pushMatrix()
                    rotateY(-PI / 2)
                    colorFaces(face, x, y)
                    popMatrix()
                if face == 5: # white
                    pushMatrix()
                    rotateX(PI / 2)
                    colorFaces(face, x, y)
                    popMatrix()
                
   
         
     # *************************************************************************************************


def colorFaces(face, x, y):
    global block
    if block[face][x][y] == 'orange': # this isnt the color, just the corresponding face
        translate(0, 0, 3 * blockSize / 2) # moves the face into the right place. this is the same for every color, as the rotation before puts it in the place
        colored(block[face][x][y]) # the function handles painting the colors correctly
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 +.5), blockColorSize, blockColorSize) # creates the rectange that is the color
    
    if block[face][x][y] == 'green': # green
        translate(0, 0, 3 * blockSize / 2)
        colored(block[face][x][y])
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 + .5), blockColorSize, blockColorSize)
    
    if block[face][x][y] == 'yellow': # white
        translate(0, 0, 3 * blockSize / 2)
        colored(block[face][x][y])
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 + .5), blockColorSize, blockColorSize)
    
    if block[face][x][y] == 'red': # yellow
        translate(0, 0, 3 * blockSize / 2)
        colored(block[face][x][y])
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 + .5), blockColorSize, blockColorSize)
    
    if block[face][x][y] == 'blue': # red
        translate(0, 0, 3 * blockSize / 2)
        colored(block[face][x][y])
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 +.5), blockColorSize, blockColorSize)
    
    if block[face][x][y] == 'white': # orange
        translate(0, 0, 3 * blockSize / 2)
        colored(block[face][x][y])
        rect(blockSize * (x - 3 / 2.0 + .5), blockSize * (y - 3 / 2.0 + .5), blockColorSize, blockColorSize)  
            
    
        # *************************************************************************************************
    

def colored(c): # handles changing the color being painted
  if c == 'green':
    fill(0, 150, 0)   # green
  if c == 'blue':
    fill(0, 100, 255) # blue
  if c == 'yellow':
    fill(200, 200, 0) # yellow
  if c == 'white':
    fill(200)         # white
  if c == 'orange':
    fill(255, 150, 0) # orange
  if c == 'red':
    fill(255, 40, 40) # red
    
    
    # *************************************************************************************************
    
    
def refreshBlock(): # this just resets block
                    # its the same array as the one in initilization
    global block    # this one is just compressed
    block = [[[Cube[2][0][0].yFace, Cube[2][0][1].yFace, Cube[2][0][2].yFace],
    [Cube[1][0][0].yFace, Cube[1][0][1].yFace, Cube[1][0][2].yFace],
    [Cube[0][0][0].yFace, Cube[0][0][1].yFace, Cube[0][0][2].yFace]],
    [[Cube[0][0][0].xFace, Cube[0][0][1].xFace, Cube[0][0][2].xFace],
    [Cube[0][1][0].xFace, Cube[0][1][1].xFace, Cube[0][1][2].xFace],
    [Cube[0][2][0].xFace, Cube[0][2][1].xFace, Cube[0][2][2].xFace]],   
    [[Cube[2][0][2].zFace, Cube[2][1][2].zFace, Cube[2][2][2].zFace],
    [Cube[1][0][2].zFace, Cube[1][1][2].zFace, Cube[1][2][2].zFace],
    [Cube[0][0][2].zFace, Cube[0][1][2].zFace, Cube[0][2][2].zFace]],    
    [[Cube[0][2][0].yFace, Cube[0][2][1].yFace, Cube[0][2][2].yFace],
    [Cube[1][2][0].yFace, Cube[1][2][1].yFace, Cube[1][2][2].yFace],
    [Cube[2][2][0].yFace, Cube[2][2][1].yFace, Cube[2][2][2].yFace]],
    [[Cube[2][2][0].xFace, Cube[2][2][1].xFace, Cube[2][2][2].xFace],
    [Cube[2][1][0].xFace, Cube[2][1][1].xFace, Cube[2][1][2].xFace],
    [Cube[2][0][0].xFace, Cube[2][0][1].xFace, Cube[2][0][2].xFace]],
    [[Cube[2][2][0].zFace, Cube[2][1][0].zFace, Cube[2][0][0].zFace],
    [Cube[1][2][0].zFace, Cube[1][1][0].zFace, Cube[1][0][0].zFace],
    [Cube[0][2][0].zFace, Cube[0][1][0].zFace, Cube[0][0][0].zFace]]]
    
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    
    
# these functions handle solving the Cube
    
    
def compare(x, y, z, arrayName): # done
    tempArray = arrayName
    if tempArray[x][y][z].name == SolvedCube[x][y][z].name and tempArray[x][y][z].xFace == SolvedCube[x][y][z].xFace:
        if tempArray[x][y][z].yFace == SolvedCube[x][y][z].yFace and tempArray[x][y][z].zFace == SolvedCube[x][y][z].zFace:
            return True
    return False
        
    
    # *************************************************************************************************
    
def solveCube():
    if cross_solved() != True:
        solve_Cross()
    
    else: 
        if f2l_solved() != True:
            solve_f2l()
        
        else:
            if OLL_solved() != True:
                solve_OLL()
            
            else:
                if OLL_solved() == True and cube_solved != True:
                    solve_PLL()
        
    
    # *************************************************************************************************
    
    
def cube_solved(arrayName): # done
    tempArray = arrayName
    
    for yCount in range(0, 4):
        establish = True
        
        for x in range(0, 3):
            for y in range(0, 3):
                for z in range(0, 3):
                    if tempArray[x][y][z].name != SolvedCube[x][y][z].name:
                        establish = False
        if establish == True:
            if yCount == 1:
                Y_(arrayName)
            elif yCount == 2:
                Y2(arrayName)
            elif yCount == 3:
                Y(arrayName)
            return True
        Y(arrayName)
    return False
    
    
    # *************************************************************************************************
    
    
def cross_solved(arrayName): # done
    # this checks the blocks and then the center piece above them, instead of rotating the cube
    tempArrayName = arrayName # i store and manipulate tempArray so the Y() moves dont do anything
    if compare(1, 0, 0, tempArrayName) == True and compare(1, 2, 0, tempArrayName) == True:
        if compare(0, 1, 0, tempArrayName) == True and compare(2, 1, 0, tempArrayName) == True: # if the 4 cross blocks are in the right place
            if tempArrayName[1][0][0].yFace == tempArrayName[1][0][1].yFace and tempArrayName[1][2][0].yFace == tempArrayName[1][2][1].yFace:
                if tempArrayName[0][1][0].xFace == tempArrayName[0][1][1].xFace and tempArrayName[2][1][0].xFace == tempArrayName[2][1][1].xFace: # if the faces match the centers
                    return True # if i hit this, the cross is solved and i return true
                
    return False 
    
    
    # *************************************************************************************************
    
    
def solve_cross(arrayName):
    firstBlockOnBottom(arrayName) # if there is a block on bottom with white face down, it will do this one first
    blocksOnTop(arrayName) 
    
    
    # *************************************************************************************************
    
    
def firstBlockOnBottom(arrayName):
    tempArray = arrayName
    
    if tempArray[1][0][0].zFace == tempArray[1][1][0].zFace: # checks if the bottom's face color is the same as the bottom center
        firstEdgeMove(1, 0, 0, arrayName)
    else:
        if tempArray[2][1][0].zFace == tempArray[1][1][0].zFace:
            firstEdgeMove(2, 1, 0, arrayName)
        else:
            if tempArray[1][2][0].zFace == tempArray[1][1][0].zFace:
                firstEdgeMove(1, 2, 0, arrayName)
            else:
                if tempArray[0][1][0].zFace == tempArray[1][1][0].zFace:
                    firstEdgeMove(0, 1, 0, arrayName)
                    
    
    # *************************************************************************************************
    
    
def firstEdgeMove(x, y, z, arrayName):
    tempArray = arrayName
    dCount = 0
    currentBlock = tempArray[x][y][z]
    
    while (currentBlock.yFace != tempArray[x][y][z + 1].name) != (tempArray[x][y][z].xFace != tempArray[x][y][z + 1].name): # if the color doesnt match center
        
        D(tempArray) # move it one
        dCount = dCount + 1 # add one to the count
        if dCount > 100:
            return 'error'
        
    if dCount == 1: # return based on dCount so its the lowest number of moves
        D(arrayName)
        return 'D'
    elif dCount == 2:
        D2(arrayName)
        return 'D2'
    elif dCount == 3:
        D_(arrayName)
        return 'D_'

    
    # *************************************************************************************************
    
def blocksOnTop(arrayName):
    pass
    
    
    
    
    # *************************************************************************************************
    
def f2l_solved(arrayName): # done
    for yCount in range(0, 4):
        establish = True
        for x in range(0, 3):
            for y in range(0, 3):
                if compare(x, y, 1, arrayName) != True or compare(x, y, 2, arrayName) != True:
                    establish = False
        if establish == True:
            if yCount == 1:
                Y_(arrayName)
            elif yCount == 2:
                Y2(arrayName)
            elif yCount == 3:
                Y(arrayName)
            return True
        Y(arrayName)
    return False             
                
    
    # *************************************************************************************************
    
    
def solve_f2l():
    pass
    
    
    # *************************************************************************************************
    
    
def OLL_solved(arrayName): # done
    tempArray = arrayName
    for x in range(0, 3):
        for y in range(0, 3):
            if tempArray[x][y][2].zFace != SolvedCube[x][y][2].zFace: # this could be written as "!= 'yellow'", but this is good i do color neutral later
                return False # if one of them arnt yellow
    return True # if all of them are yellow i hit this
    
    # *************************************************************************************************
    
    
def solve_OLL():
    pass
    
    
    # *************************************************************************************************
    
    
def solve_PLL():
    pass
    
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    
    
# these handle clicks or other various things
    
    
def mouseClicked(): # if the mouse is clicked, it changes the value of viewState
                    # which is interpreted in DRAW to change the camera mode
    global viewState
    
    if viewState == 'locked':
        viewState = 'free'
    
    elif viewState == 'free':
        viewState = 'locked'

    
     # *************************************************************************************************   


def scramble(): # generates a random 25 move scramble in list format that i can quickly run through for an initial scramble
    scramble_length = 25
    moves = ["R", "R_", "R2", "L", "L_", "L2", "U", "U_", "U2", "D", "D_", "D2", "F", "F_", "F2", "B", "B_", "B2"]  
    scramble = []
    
    for i in range(0, scramble_length + 1):
        random_move = random.randint(0, len(moves) - 1)
        
        if i > 0:
            while moves[random_move][0] == prev_move[0]:
                random_move = random.randint(0, len(moves) - 1)      
        
        scramble.append(moves[random_move])
        prev_move = moves[random_move]
    return scramble
     
     
     # *************************************************************************************************

     
# gets run by draw if a key is released, it is here for easier reading and a smaller draw funtion

def keyPressed(): # the test_ori print the blocks position and orientation to the console for debugging, they can be removed at a later date
    if key == '\n':
        if CubeSolved() == False:
            solveCube()
    elif key == '1':
        firstBlockOnBottom(Cube)
    elif key == 'r': # single moves
        R(Cube)
    elif key == 'R':
        R_(Cube)
    elif key == 'L':
        L_(Cube)
    elif key == 'l':
        L(Cube)
    elif key == 'f':
        F(Cube)
    elif key == 'F':
        F_(Cube)
    elif key == 'b':
        B(Cube)
    elif key == 'B':
        B_(Cube)
    elif key == 'u':
        U(Cube)
    elif key == 'U':
        U_(Cube)
    elif key == 'd':
        D(Cube)
    elif key == 'D':
        D_(Cube)
    elif key == 'm': # middle moves
        M(Cube)
    elif key == 'M':
        M_(Cube)
    elif key == 's':
        S(Cube)
    elif key == 'S':
        S_(Cube)
    elif key == 'e':
        E(Cube)
    elif key == 'E':
        E_(Cube)
    elif key == 'x': # rotations
        X(Cube)
    elif key == 'X':
        X_(Cube)
    elif key == 'y':
        Y(Cube)
    elif key == 'Y':
        Y_(Cube)
    elif key == 'z':
        Z(Cube)
    elif key == 'Z':
        Z_(Cube)
    elif key == ' ':
        applyScramble()


    # *************************************************************************************************
    
    
def applyScramble():
    sk = scramble()
    for move in sk:
        if move == 'R':
            R(Cube)
        elif move == 'R_':
            R_(Cube)
        elif move == 'L_':
            L_(Cube)
        elif move == 'L':
            L(Cube)
        elif move == 'F':
            F(Cube)
        elif move == 'F_':
            F_(Cube)
        elif move == 'B':
            B(Cube)
        elif move == 'B_':
            B_(Cube)
        elif move == 'U':
            U(Cube)
        elif move == 'U_':
            U_(Cube)
            
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    
# these functions handle turning the Cube 


def R(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[2][0][1]
    arrayName[2][0][1]      = arrayName[2][1][0]
    arrayName[2][1][0]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[2][1][2]
    arrayName[2][1][2]      = subs

    # corners
    subs               = arrayName[2][0][0]
    arrayName[2][0][0]      = arrayName[2][2][0]
    arrayName[2][2][0]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[2][0][2]
    arrayName[2][0][2]      = subs

    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[2][yPos][zPos].yFace
            arrayName[2][yPos][zPos].yFace = arrayName[2][yPos][zPos].zFace
            arrayName[2][yPos][zPos].zFace = subs
                           
          
  # *************************************************************************************************  
  
  
def R_(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[2][0][1]
    arrayName[2][0][1]      = arrayName[2][1][2]
    arrayName[2][1][2]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[2][1][0]
    arrayName[2][1][0]      = subs

    # corners
    subs               = arrayName[2][0][0]
    arrayName[2][0][0]      = arrayName[2][0][2]
    arrayName[2][0][2]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[2][2][0]
    arrayName[2][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[2][yPos][zPos].yFace
            arrayName[2][yPos][zPos].yFace = arrayName[2][yPos][zPos].zFace
            arrayName[2][yPos][zPos].zFace = subs
    
    
    # *************************************************************************************************
  
  
def R2(arrayName):
    R(arrayName)
    R(arrayName)  
  
  
    # *************************************************************************************************  
  
  
def L(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[0][1][2]
    arrayName[0][1][2]      = arrayName[0][2][1]
    arrayName[0][2][1]      = arrayName[0][1][0]
    arrayName[0][1][0]      = subs

    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[0][0][2]
    arrayName[0][0][2]      = arrayName[0][2][2]
    arrayName[0][2][2]      = arrayName[0][2][0]
    arrayName[0][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[0][yPos][zPos].yFace
            arrayName[0][yPos][zPos].yFace = arrayName[0][yPos][zPos].zFace
            arrayName[0][yPos][zPos].zFace = subs
    
  
  # *************************************************************************************************  
  
  
def L_(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[0][1][0]
    arrayName[0][1][0]      = arrayName[0][2][1]
    arrayName[0][2][1]      = arrayName[0][1][2]
    arrayName[0][1][2]      = subs

    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[0][2][0]
    arrayName[0][2][0]      = arrayName[0][2][2]
    arrayName[0][2][2]      = arrayName[0][0][2]
    arrayName[0][0][2]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[0][yPos][zPos].yFace
            arrayName[0][yPos][zPos].yFace = arrayName[0][yPos][zPos].zFace
            arrayName[0][yPos][zPos].zFace = subs
        
        
    # *************************************************************************************************  
  
  
def L2(arrayName):
    L(arrayName)
    L(arrayName)  
  
  
    # *************************************************************************************************


def F(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[1][0][0]
    arrayName[1][0][0]      = arrayName[2][0][1]
    arrayName[2][0][1]      = arrayName[1][0][2]
    arrayName[1][0][2]      = subs

    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[2][0][0]
    arrayName[2][0][0]      = arrayName[2][0][2]
    arrayName[2][0][2]      = arrayName[0][0][2]
    arrayName[0][0][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][0][zPos].xFace
            arrayName[xPos][0][zPos].xFace = arrayName[xPos][0][zPos].zFace
            arrayName[xPos][0][zPos].zFace = subs
        
        
        # *************************************************************************************************  
  
  
def F_(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[1][0][2]
    arrayName[1][0][2]      = arrayName[2][0][1]
    arrayName[2][0][1]      = arrayName[1][0][0]
    arrayName[1][0][0]      = subs

    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[0][0][2]
    arrayName[0][0][2]      = arrayName[2][0][2]
    arrayName[2][0][2]      = arrayName[2][0][0]
    arrayName[2][0][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][0][zPos].xFace
            arrayName[xPos][0][zPos].xFace = arrayName[xPos][0][zPos].zFace
            arrayName[xPos][0][zPos].zFace = subs
     
        
    # *************************************************************************************************


def F2(arrayName):
    F(arrayName)
    F(arrayName)  
  
  
    # *************************************************************************************************
    
   
def B(arrayName): 
    global Cube

    # edges
    subs               = arrayName[0][2][1]
    arrayName[0][2][1]      = arrayName[1][2][2]
    arrayName[1][2][2]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[1][2][0]
    arrayName[1][2][0]      = subs
    
    # corners
    subs               = arrayName[0][2][0]
    arrayName[0][2][0]      = arrayName[0][2][2]
    arrayName[0][2][2]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[2][2][0]
    arrayName[2][2][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][2][zPos].xFace
            arrayName[xPos][2][zPos].xFace = arrayName[xPos][2][zPos].zFace
            arrayName[xPos][2][zPos].zFace = subs
    
        
    # *************************************************************************************************
    
    
def B_(arrayName): 
    global Cube

    # edges
    subs               = arrayName[0][2][1]
    arrayName[0][2][1]      = arrayName[1][2][0]
    arrayName[1][2][0]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[1][2][2]
    arrayName[1][2][2]      = subs
    
    # corners
    subs               = arrayName[0][2][0]
    arrayName[0][2][0]      = arrayName[2][2][0]
    arrayName[2][2][0]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[0][2][2]
    arrayName[0][2][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][2][zPos].xFace
            arrayName[xPos][2][zPos].xFace = arrayName[xPos][2][zPos].zFace
            arrayName[xPos][2][zPos].zFace = subs
    
        
    # *************************************************************************************************
    
    
def B2(arrayName):
    B(arrayName)
    B(arrayName)
    
    
    # *************************************************************************************************
    
    
def U(arrayName): 
    global Cube

    # edges
    subs               = arrayName[1][0][2]
    arrayName[1][0][2]      = arrayName[2][1][2]
    arrayName[2][1][2]      = arrayName[1][2][2]
    arrayName[1][2][2]      = arrayName[0][1][2]
    arrayName[0][1][2]      = subs
    
    # corners
    subs               = arrayName[0][0][2]
    arrayName[0][0][2]      = arrayName[2][0][2]
    arrayName[2][0][2]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[0][2][2]
    arrayName[0][2][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][2].xFace
            arrayName[xPos][yPos][2].xFace = arrayName[xPos][yPos][2].yFace
            arrayName[xPos][yPos][2].yFace = subs
        
        
    # *************************************************************************************************
    
    
def U_(arrayName):
    global Cube

    # edges
    subs               = arrayName[1][0][2]
    arrayName[1][0][2]      = arrayName[0][1][2]
    arrayName[0][1][2]      = arrayName[1][2][2]
    arrayName[1][2][2]      = arrayName[2][1][2]
    arrayName[2][1][2]      = subs
    
    # corners
    subs               = arrayName[0][0][2]
    arrayName[0][0][2]      = arrayName[0][2][2]
    arrayName[0][2][2]      = arrayName[2][2][2]
    arrayName[2][2][2]      = arrayName[2][0][2]
    arrayName[2][0][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][2].xFace
            arrayName[xPos][yPos][2].xFace = arrayName[xPos][yPos][2].yFace
            arrayName[xPos][yPos][2].yFace = subs
        
        
# *************************************************************************************************


def U2(arrayName):
    U(arrayName)
    U(arrayName)
    
    
# *************************************************************************************************


def D(arrayName): 
    global Cube

    # edges
    subs               = arrayName[1][0][0]
    arrayName[1][0][0]      = arrayName[0][1][0]
    arrayName[0][1][0]      = arrayName[1][2][0]
    arrayName[1][2][0]      = arrayName[2][1][0]
    arrayName[2][1][0]      = subs
    
    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[0][2][0]
    arrayName[0][2][0]      = arrayName[2][2][0]
    arrayName[2][2][0]      = arrayName[2][0][0]
    arrayName[2][0][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][0].xFace
            arrayName[xPos][yPos][0].xFace = arrayName[xPos][yPos][0].yFace
            arrayName[xPos][yPos][0].yFace = subs
        
        
# *************************************************************************************************


def D_(arrayName): 
    global Cube

    # edges
    subs               = arrayName[1][0][0]
    arrayName[1][0][0]      = arrayName[2][1][0]
    arrayName[2][1][0]      = arrayName[1][2][0]
    arrayName[1][2][0]      = arrayName[0][1][0]
    arrayName[0][1][0]      = subs
    
    # corners
    subs               = arrayName[0][0][0]
    arrayName[0][0][0]      = arrayName[2][0][0]
    arrayName[2][0][0]      = arrayName[2][2][0]
    arrayName[2][2][0]      = arrayName[0][2][0]
    arrayName[0][2][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][0].xFace
            arrayName[xPos][yPos][0].xFace = arrayName[xPos][yPos][0].yFace
            arrayName[xPos][yPos][0].yFace = subs
        
        
    # *************************************************************************************************
    
    
def D2(arrayName):
    D(arrayName)
    D(arrayName)
    
    
    # *************************************************************************************************


def M(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[1][0][1]
    arrayName[1][0][1]      = arrayName[1][1][2]
    arrayName[1][1][2]      = arrayName[1][2][1]
    arrayName[1][2][1]      = arrayName[1][1][0]
    arrayName[1][1][0]      = subs

    # corners
    subs               = arrayName[1][0][0]
    arrayName[1][0][0]      = arrayName[1][0][2]
    arrayName[1][0][2]      = arrayName[1][2][2]
    arrayName[1][2][2]      = arrayName[1][2][0]
    arrayName[1][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[1][yPos][zPos].yFace
            arrayName[1][yPos][zPos].yFace = arrayName[1][yPos][zPos].zFace
            arrayName[1][yPos][zPos].zFace = subs
    
    
    # *************************************************************************************************


def M_(arrayName): 
    global Cube
    
    
    # edges
    subs               = arrayName[1][0][1]
    arrayName[1][0][1]      = arrayName[1][1][0]
    arrayName[1][1][0]      = arrayName[1][2][1]
    arrayName[1][2][1]      = arrayName[1][1][2]
    arrayName[1][1][2]      = subs

    # corners
    subs               = arrayName[1][0][0]
    arrayName[1][0][0]      = arrayName[1][2][0]
    arrayName[1][2][0]      = arrayName[1][2][2]
    arrayName[1][2][2]      = arrayName[1][0][2]
    arrayName[1][0][2]      = subs

    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[1][yPos][zPos].yFace
            arrayName[1][yPos][zPos].yFace = arrayName[1][yPos][zPos].zFace
            arrayName[1][yPos][zPos].zFace = subs
                          
          
  # *************************************************************************************************  


def M2(arrayName):
    M(arrayName)
    M(arrayName)


    # *************************************************************************************************


def E(arrayName): 
    global Cube

    # edges
    subs               = arrayName[1][0][1]
    arrayName[1][0][1]      = arrayName[0][1][1]
    arrayName[0][1][1]      = arrayName[1][2][1]
    arrayName[1][2][1]      = arrayName[2][1][1]
    arrayName[2][1][1]      = subs
    
    # corners
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[0][2][1]
    arrayName[0][2][1]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[2][0][1]
    arrayName[2][0][1]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][1].xFace
            arrayName[xPos][yPos][1].xFace = arrayName[xPos][yPos][1].yFace
            arrayName[xPos][yPos][1].yFace = subs


    # *************************************************************************************************


def E_(arrayName): 
    global Cube

    # edges
    subs               = arrayName[1][0][1]
    arrayName[1][0][1]      = arrayName[2][1][1]
    arrayName[2][1][1]      = arrayName[1][2][1]
    arrayName[1][2][1]      = arrayName[0][1][1]
    arrayName[0][1][1]      = subs
    
    # corners
    subs               = arrayName[0][0][1]
    arrayName[0][0][1]      = arrayName[2][0][1]
    arrayName[2][0][1]      = arrayName[2][2][1]
    arrayName[2][2][1]      = arrayName[0][2][1]
    arrayName[0][2][1]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = arrayName[xPos][yPos][1].xFace
            arrayName[xPos][yPos][1].xFace = arrayName[xPos][yPos][1].yFace
            arrayName[xPos][yPos][1].yFace = subs
        
        
    # *************************************************************************************************


def E2(arrayName):
    E(arrayName)
    E(arrayName)


    # *************************************************************************************************


def S(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][1][1]
    arrayName[0][1][1]      = arrayName[1][1][0]
    arrayName[1][1][0]      = arrayName[2][1][1]
    arrayName[2][1][1]      = arrayName[1][1][2]
    arrayName[1][1][2]      = subs

    # corners
    subs               = arrayName[0][1][0]
    arrayName[0][1][0]      = arrayName[2][1][0]
    arrayName[2][1][0]      = arrayName[2][1][2]
    arrayName[2][1][2]      = arrayName[0][1][2]
    arrayName[0][1][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][1][zPos].xFace
            arrayName[xPos][1][zPos].xFace = arrayName[xPos][1][zPos].zFace
            arrayName[xPos][1][zPos].zFace = subs
        
        
        # *************************************************************************************************  
  
  
def S_(arrayName): 
    global Cube
    
    # edges
    subs               = arrayName[0][1][1]
    arrayName[0][1][1]      = arrayName[1][1][2]
    arrayName[1][1][2]      = arrayName[2][1][1]
    arrayName[2][1][1]      = arrayName[1][1][0]
    arrayName[1][1][0]      = subs

    # corners
    subs               = arrayName[0][1][0]
    arrayName[0][1][0]      = arrayName[0][1][2]
    arrayName[0][1][2]      = arrayName[2][1][2]
    arrayName[2][1][2]      = arrayName[2][1][0]
    arrayName[2][1][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = arrayName[xPos][1][zPos].xFace
            arrayName[xPos][1][zPos].xFace = arrayName[xPos][1][zPos].zFace
            arrayName[xPos][1][zPos].zFace = subs
     
        
    # *************************************************************************************************


def S2(arrayName):
    S(arrayName)
    S(arrayName)  
  
  
    # *************************************************************************************************


def r(arrayName): 
    R(arrayName)
    M_(arrayName)


    # *************************************************************************************************


def r_(arrayName): 
    R_(arrayName)
    M(arrayName)


    # *************************************************************************************************

    
def r2(arrayName): 
    r(arrayName)
    r(arrayName)
    

    # *************************************************************************************************
    
    
def l(arrayName): 
    L(arrayName)
    M(arrayName)


    # *************************************************************************************************


def l_(arrayName): 
    L_(arrayName)
    M_(arrayName)


    # *************************************************************************************************

    
def l2(arrayName): 
    l(arrayName)
    l(arrayName)


    # *************************************************************************************************
    

def u(arrayName): 
    U(arrayName)
    E_(arrayName)


    # *************************************************************************************************


def u_(arrayName): 
    U_(arrayName)
    E(arrayName)


    # *************************************************************************************************

    
def u2(arrayName): 
    u(arrayName)
    u(arrayName)


    # *************************************************************************************************
    

def d(arrayName): 
    D(arrayName)
    E(arrayName)


    # *************************************************************************************************


def d_(arrayName): 
    D_(arrayName)
    E_(arrayName)


    # *************************************************************************************************

    
def d2(arrayName): 
    d(arrayName)
    d(arrayName)


    # *************************************************************************************************

    
def f(arrayName): 
    F(arrayName)
    S(arrayName)


    # *************************************************************************************************


def f_(arrayName): 
    F_(arrayName)
    S_(arrayName)


    # *************************************************************************************************

    
def f2(arrayName): 
    f(arrayName)
    f(arrayName)


    # *************************************************************************************************
    
  
def b(arrayName): 
    B(arrayName)
    S_(arrayName)


    # *************************************************************************************************
    

def b_(arrayName): 
    B_(arrayName)
    S(arrayName)


    # *************************************************************************************************


def b2(arrayName): 
    b(arrayName)
    b(arrayName)

    # *************************************************************************************************

    
def X(arrayName): 
    R(arrayName)
    l_(arrayName)


    # *************************************************************************************************


def X_(arrayName): 
    R_(arrayName)
    l(arrayName)


    # *************************************************************************************************

    
def X2(arrayName): 
    X(arrayName)
    X(arrayName)


    # *************************************************************************************************
    

def Y(arrayName): 
    U(arrayName)
    d_(arrayName)


    # *************************************************************************************************


def Y_(arrayName): 
    U_(arrayName)
    d(arrayName)


    # *************************************************************************************************

    
def Y2(arrayName): 
    Y(arrayName)
    Y(arrayName)


    # *************************************************************************************************
    

def Z(arrayName): 
    F(arrayName)
    b_(arrayName)


    # *************************************************************************************************


def Z_(arrayName): 
    F_(arrayName)
    b(arrayName)


    # *************************************************************************************************
    
    
def Z2(arrayName): 
    Z(arrayName)
    Z(arrayName)


    # *************************************************************************************************

    
