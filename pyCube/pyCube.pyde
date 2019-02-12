# space scrambles the arrayName randomly
# r, u, b, etc, move the arrayName in there respective ways
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
        

# creating the blocks, set up in the same format as arrayName 
white_orange_green =     Block('white_orange_green',           'corner',   'green',   'orange',   'white')
orange_green =           Block('orange_green',                 'edge',     'green',   'orange',   None)
yellow_orange_green =    Block('yellow_orange_green',          'corner',   'green',   'orange',   'yellow')
    
white_green =            Block('white_green',                  'edge',     'green',   None,       'white')
green_ =                 Block('green_',                       'center',   'green',   None,       None)
yellow_green =           Block('yellow_green',                 'edge',     'green',   None,       'yellow')
    
white_red_green =        Block('white_red_green',              'corner',   'green',   'red',      'white')
red_green =              Block('red_green',                    'edge',     'green',   'red',      None)
yellow_red_green =       Block('yellow_red_green',             'corner',   'green',   'red',      'yellow')
    
    
white_orange =           Block('white_orange',                 'edge',     None,      'orange',   'white')
orange_ =                Block('orange_',                      'center',   None,      'orange',   None)
yellow_orange =          Block('yellow_orange',                'edge',     None,      'orange',   'yellow')
    
white_ =                 Block('white_',                       'center',   None,      None,       'white')
core =                   Block('core',                         'core',     None,      None,       None)
yellow_ =                Block('yellow_',                      'center',   None,      None,       'yellow')
    
white_red =              Block('white_red',                    'edge',     None,      'red',      'white')
red_ =                   Block('red_',                         'center',   None,      'red',      None)
yellow_red =             Block('yellow_red',                   'edge',     None,      'red',      'yellow')
    
    
white_orange_blue =      Block('white_orange_blue',            'corner',   'blue',    'orange',   'white')
orange_blue =            Block('orange_blue',                  'edge',     'blue',    'orange',   None)
yellow_orange_blue =     Block('yellow_orange_blue',           'corner',   'blue',    'orange',   'yellow')
    
white_blue =             Block('white_blue',                   'edge',     'blue',    None,       'white')
blue_ =                  Block('blue_',                        'center',   'blue',    None,       None)
yellow_blue =            Block('yellow_blue',                  'edge',     'blue',    None,       'yellow')
    
white_red_blue =         Block('white_red_blue',               'corner',   'blue',    'red',      'white')
red_blue =               Block('red_blue',                     'edge',     'blue',    'red',      None)
yellow_red_blue =        Block('yellow_red_blue',              'corner',   'blue',    'red',      'yellow')
    
    
    # arrayName array
arrayName = [# this is the actual setup for the arrayName, and can be used to figure out what is where
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

# this is a 3d list that takes the faces of each side so that the arrayName visualation is integrated

block = [ #### if you change this list change the one in refreshBlock(arrayName) ####
    [ # orange
    [arrayName[2][0][0].yFace, arrayName[2][0][1].yFace, arrayName[2][0][2].yFace],
    [arrayName[1][0][0].yFace, arrayName[1][0][1].yFace, arrayName[1][0][2].yFace],
    [arrayName[0][0][0].yFace, arrayName[0][0][1].yFace, arrayName[0][0][2].yFace]
    ],
    [ # green
    [arrayName[0][0][0].xFace, arrayName[0][0][1].xFace, arrayName[0][0][2].xFace],
    [arrayName[0][1][0].xFace, arrayName[0][1][1].xFace, arrayName[0][1][2].xFace],
    [arrayName[0][2][0].xFace, arrayName[0][2][1].xFace, arrayName[0][2][2].xFace]
    ],   
    [ # yellow
    [arrayName[2][0][2].zFace, arrayName[2][1][2].zFace, arrayName[2][2][2].zFace],
    [arrayName[1][0][2].zFace, arrayName[1][1][2].zFace, arrayName[1][2][2].zFace],
    [arrayName[0][0][2].zFace, arrayName[0][1][2].zFace, arrayName[0][2][2].zFace]
    ],    
    [ # red
    [arrayName[0][2][0].yFace, arrayName[0][2][1].yFace, arrayName[0][2][2].yFace],
    [arrayName[1][2][0].yFace, arrayName[1][2][1].yFace, arrayName[1][2][2].yFace],
    [arrayName[2][2][0].yFace, arrayName[2][2][1].yFace, arrayName[2][2][2].yFace]
    ],
    [ # blue
    [arrayName[2][2][0].xFace, arrayName[2][2][1].xFace, arrayName[2][2][2].xFace],
    [arrayName[2][1][0].xFace, arrayName[2][1][1].xFace, arrayName[2][1][2].xFace],
    [arrayName[2][0][0].xFace, arrayName[2][0][1].xFace, arrayName[2][0][2].xFace]
    ],
    [ # white
    [arrayName[2][2][0].zFace, arrayName[2][1][0].zFace, arrayName[2][0][0].zFace],
    [arrayName[1][2][0].zFace, arrayName[1][1][0].zFace, arrayName[1][0][0].zFace],
    [arrayName[0][2][0].zFace, arrayName[0][1][0].zFace, arrayName[0][0][0].zFace]
    ]]
 
 
SolvedarrayName = [[[ white_orange_green, orange_green, yellow_orange_green ], 
[ white_green, green_, yellow_green ],
[ white_red_green, red_green, yellow_red_green ]],
[[ white_orange, orange_, yellow_orange ], 
[ white_, core, yellow_ ],
[ white_red, red_, yellow_red ]],
[[ white_orange_blue, orange_blue, yellow_orange_blue ], 
[ white_blue, blue_, yellow_blue ],
[ white_red_blue, red_blue, yellow_red_blue ]]]          
    
SolvedBlock = [[[SolvedarrayName[2][0][0].yFace, SolvedarrayName[2][0][1].yFace, SolvedarrayName[2][0][2].yFace],
[SolvedarrayName[1][0][0].yFace, SolvedarrayName[1][0][1].yFace, SolvedarrayName[1][0][2].yFace],
[SolvedarrayName[0][0][0].yFace, SolvedarrayName[0][0][1].yFace, SolvedarrayName[0][0][2].yFace]],
[[SolvedarrayName[0][0][0].xFace, SolvedarrayName[0][0][1].xFace, SolvedarrayName[0][0][2].xFace],
[SolvedarrayName[0][1][0].xFace, SolvedarrayName[0][1][1].xFace, SolvedarrayName[0][1][2].xFace],
[SolvedarrayName[0][2][0].xFace, SolvedarrayName[0][2][1].xFace, SolvedarrayName[0][2][2].xFace]],   
[[SolvedarrayName[2][0][2].zFace, SolvedarrayName[2][1][2].zFace, SolvedarrayName[2][2][2].zFace],
[SolvedarrayName[1][0][2].zFace, SolvedarrayName[1][1][2].zFace, SolvedarrayName[1][2][2].zFace],
[SolvedarrayName[0][0][2].zFace, SolvedarrayName[0][1][2].zFace, SolvedarrayName[0][2][2].zFace]],    
[[SolvedarrayName[0][2][0].yFace, SolvedarrayName[0][2][1].yFace, SolvedarrayName[0][2][2].yFace],
[SolvedarrayName[1][2][0].yFace, SolvedarrayName[1][2][1].yFace, SolvedarrayName[1][2][2].yFace],
[SolvedarrayName[2][2][0].yFace, SolvedarrayName[2][2][1].yFace, SolvedarrayName[2][2][2].yFace]],
[[SolvedarrayName[2][2][0].xFace, SolvedarrayName[2][2][1].xFace, SolvedarrayName[2][2][2].xFace],
[SolvedarrayName[2][1][0].xFace, SolvedarrayName[2][1][1].xFace, SolvedarrayName[2][1][2].xFace],
[SolvedarrayName[2][0][0].xFace, SolvedarrayName[2][0][1].xFace, SolvedarrayName[2][0][2].xFace]],
[[SolvedarrayName[2][2][0].zFace, SolvedarrayName[2][1][0].zFace, SolvedarrayName[2][0][0].zFace],
[SolvedarrayName[1][2][0].zFace, SolvedarrayName[1][1][0].zFace, SolvedarrayName[1][0][0].zFace],
[SolvedarrayName[0][2][0].zFace, SolvedarrayName[0][1][0].zFace, SolvedarrayName[0][0][0].zFace]]]


# *************************************************************************************************
    
    
def setup(arrayName): # this only runs once
    
    size(600, 600, P3D) # creates window in 3d mode 
    strokeWeight(5)
    noFill(arrayName)
    rectMode(CENTER)

    
# *************************************************************************************************


def draw(arrayName):
    background(100, 100, 150) # background color
    translate(width / 2, height / 2) # moves the arrayName so its actually in the frame
    fill(255)
    
    if viewState == 'free': # becasue of the way camera stuff works, this needs to be in draw
        rotateX(-mouseY * PI / 300)    # when you click the mouse, a function changes the variable viewState
        rotateY(mouseX * PI / 300)     # this top code follows mouse
    else:
        rotateX((3 * PI / 4) + (PI / 16)) # the arrayName is set to a default position, which is + PI / 16 off normal
        rotateY((3 * PI / 4) + (PI / 16))

    createarrayNameVisual(arrayName)
    
    
    
    # *************************************************************************************************
    
    
def createarrayNameVisual(arrayName):        
    global Cube
    global block
    refreshBlock(arrayName) # updates the block array to the correct config
    
    for face in range(0, 6): # runs through the colors
        for x in range(0, 3): # creates a triple nested loop, the outside 2 loops run 3 times, the inside one runs 6 times
            for y in range(0, 3): # they run through and create all of the colors needed at the correct positionsr
                if face == 0: # orange
                    pushMatrix(arrayName) # retrives a default pos
                    # no rotation
                    colorFaces(face, x, y) # this draw the face we are on, in this case its orange
                    popMatrix(arrayName) # undos the default pos
                if face == 1: # green
                    pushMatrix(arrayName)
                    rotateY(PI / 2)
                    colorFaces(face, x, y)
                    popMatrix(arrayName)
                if face == 2: # yellow
                    pushMatrix(arrayName)
                    rotateX(-PI / 2)
                    colorFaces(face, x, y)
                    popMatrix(arrayName)
                if face == 3: # red
                    pushMatrix(arrayName)
                    rotateY(PI)
                    colorFaces(face, x, y)
                    popMatrix(arrayName)
                if face == 4: # blue
                    pushMatrix(arrayName)
                    rotateY(-PI / 2)
                    colorFaces(face, x, y)
                    popMatrix(arrayName)
                if face == 5: # white
                    pushMatrix(arrayName)
                    rotateX(PI / 2)
                    colorFaces(face, x, y)
                    popMatrix(arrayName)
                
   
         
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
    
    
def refreshBlock(arrayName): # this just resets block
                    # its the same array as the one in initilization
    global block    # this one is just compressed
    block = [[[arrayName[2][0][0].yFace, arrayName[2][0][1].yFace, arrayName[2][0][2].yFace],
    [arrayName[1][0][0].yFace, arrayName[1][0][1].yFace, arrayName[1][0][2].yFace],
    [arrayName[0][0][0].yFace, arrayName[0][0][1].yFace, arrayName[0][0][2].yFace]],
    [[arrayName[0][0][0].xFace, arrayName[0][0][1].xFace, arrayName[0][0][2].xFace],
    [arrayName[0][1][0].xFace, arrayName[0][1][1].xFace, arrayName[0][1][2].xFace],
    [arrayName[0][2][0].xFace, arrayName[0][2][1].xFace, arrayName[0][2][2].xFace]],   
    [[arrayName[2][0][2].zFace, arrayName[2][1][2].zFace, arrayName[2][2][2].zFace],
    [arrayName[1][0][2].zFace, arrayName[1][1][2].zFace, arrayName[1][2][2].zFace],
    [arrayName[0][0][2].zFace, arrayName[0][1][2].zFace, arrayName[0][2][2].zFace]],    
    [[arrayName[0][2][0].yFace, arrayName[0][2][1].yFace, arrayName[0][2][2].yFace],
    [arrayName[1][2][0].yFace, arrayName[1][2][1].yFace, arrayName[1][2][2].yFace],
    [arrayName[2][2][0].yFace, arrayName[2][2][1].yFace, arrayName[2][2][2].yFace]],
    [[arrayName[2][2][0].xFace, arrayName[2][2][1].xFace, arrayName[2][2][2].xFace],
    [arrayName[2][1][0].xFace, arrayName[2][1][1].xFace, arrayName[2][1][2].xFace],
    [arrayName[2][0][0].xFace, arrayName[2][0][1].xFace, arrayName[2][0][2].xFace]],
    [[arrayName[2][2][0].zFace, arrayName[2][1][0].zFace, arrayName[2][0][0].zFace],
    [arrayName[1][2][0].zFace, arrayName[1][1][0].zFace, arrayName[1][0][0].zFace],
    [arrayName[0][2][0].zFace, arrayName[0][1][0].zFace, arrayName[0][0][0].zFace]]]
    
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # these functions handle solving the arrayName
    
    
def arrayNameNotSolved(arrayName):
    if arrayName == SolvedarrayName and block == SolvedBlock:
        return False
    else:
        return True


    # *************************************************************************************************
    
    
def compareBlocks(x, y, z):
    if arrayName[x][y][z] == solvedarrayName[x][y][z]:
        if arrayName[x][y][z].xFace == solvedarrayName[x][y][z].xFace and arrayName[x][y][z].yFace == solvedarrayName[x][y][z].yFace and arrayName[x][y][z].zFace == arrayName[x][y][z].zFace:
            return True
        else:
            return False
    else:
        return False
    
    
    # *************************************************************************************************
    
def solvearrayName(arrayName):
    if cross_Not_Solved(arrayName):
        solve_Cross(arrayName)
    
    elif f2l_Not_Solved(arrayName):
        solve_f2l(arrayName)
    
    elif OLL_Not_Solved(arrayName):
        solve_OLL(arrayName)
    
    elif PLL_Not_Solved(arrayName):
        solve_PLL
        
    
    # *************************************************************************************************
    
def cross_Not_Solved(arrayName):
    for y in range(0, 2):
        if compare(1, y, 0) != True:
            return False
    for x in range(0, 2):
        if compare(x, 1, 0) != True:
            return False
    return True
        
    
    
    # *************************************************************************************************
    
    
def solve_Cross(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def f2l_Not_Solved(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def solve_f2l(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def OLL_Not_Solved(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def solve_OLL(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def PLL_Not_Solved(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
def solve_PLL(arrayName):
    pass
    
    
    # *************************************************************************************************
    
    
    
    
    
    
    
    
    # *************************************************************************************************
    
    
def mouseClicked(arrayName): # if the mouse is clicked, it changes the value of viewState
                    # which is interpreted in DRAW to change the camera mode
    global viewState
    
    if viewState == 'locked':
        viewState = 'free'
    
    elif viewState == 'free':
        viewState = 'locked'

    
     # *************************************************************************************************   


def scramble(arrayName): # generates a random 25 move scramble in list format that i can quickly run through for an initial scramble
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

def keyPressed(arrayName): # the test_ori print the blocks position and orientation to the console for debugging, they can be removed at a later date
    if key == '\n':
        if arrayNameNotSolved(arrayName):
            solvearrayName(arrayName)
    elif key == 'r': # single moves
        R(arrayName)
    elif key == 'R':
        R_(arrayName)
    elif key == 'L':
        L_(arrayName)
    elif key == 'l':
        L(arrayName)
    elif key == 'f':
        F(arrayName)
    elif key == 'F':
        F_(arrayName)
    elif key == 'b':
        B(arrayName)
    elif key == 'B':
        B_(arrayName)
    elif key == 'u':
        U(arrayName)
    elif key == 'U':
        U_(arrayName)
    elif key == 'd':
        D(arrayName)
    elif key == 'D':
        D_(arrayName)
    elif key == 'm': # middle moves
        M(arrayName)
    elif key == 'M':
        M_(arrayName)
    elif key == 's':
        S(arrayName)
    elif key == 'S':
        S_(arrayName)
    elif key == 'e':
        E(arrayName)
    elif key == 'E':
        E_(arrayName)
    elif key == 'x': # rotations
        X(arrayName)
    elif key == 'X':
        X_(arrayName)
    elif key == 'y':
        Y(arrayName)
    elif key == 'Y':
        Y_(arrayName)
    elif key == 'z':
        Z(arrayName)
    elif key == 'Z':
        Z_(arrayName)
    elif key == ' ':
        applyScramble(arrayName)


    # *************************************************************************************************
    
    
def applyScramble(arrayName):
    sk = scramble(arrayName)
    for move in sk:
        if move == 'R':
            R(arrayName)
        elif move == 'R_':
            R_(arrayName)
        elif move == 'L_':
            L_(arrayName)
        elif move == 'L':
            L(arrayName)
        elif move == 'F':
            F(arrayName)
        elif move == 'F_':
            F_(arrayName)
        elif move == 'B':
            B(arrayName)
        elif move == 'B_':
            B_(arrayName)
        elif move == 'U':
            U(arrayName)
        elif move == 'U_':
            U_(arrayName)
            
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # these functions handle turning the arrayName 


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

    
