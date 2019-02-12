# space scrambles the cube randomly
# r, u, b, etc, move the cube in there respective ways
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
        

# creating the blocks, set up in the same format as Cube 
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
    
    
    # cube array
Cube = [# this is the actual setup for the cube, and can be used to figure out what is where
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

# this is a 3d list that takes the faces of each side so that the cube visualation is integrated

block = [ #### if you change this list change the one in refreshBlock() ####
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
 
 
SolvedCube = [[[ white_orange_green, orange_green, yellow_orange_green ], 
[ white_green, green_, yellow_green ],
[ white_red_green, red_green, yellow_red_green ]],
[[ white_orange, orange_, yellow_orange ], 
[ white_, core, yellow_ ],
[ white_red, red_, yellow_red ]],
[[ white_orange_blue, orange_blue, yellow_orange_blue ], 
[ white_blue, blue_, yellow_blue ],
[ white_red_blue, red_blue, yellow_red_blue ]]]          
    
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
    
    
def setup(): # this only runs once
    
    size(600, 600, P3D) # creates window in 3d mode 
    strokeWeight(5)
    noFill()
    rectMode(CENTER)

    
# *************************************************************************************************


def draw():
    background(100, 100, 150) # background color
    translate(width / 2, height / 2) # moves the cube so its actually in the frame
    fill(255)
    
    if viewState == 'free': # becasue of the way camera stuff works, this needs to be in draw
        rotateX(-mouseY * PI / 300)    # when you click the mouse, a function changes the variable viewState
        rotateY(mouseX * PI / 300)     # this top code follows mouse
    else:
        rotateX((3 * PI / 4) + (PI / 16)) # the cube is set to a default position, which is + PI / 16 off normal
        rotateY((3 * PI / 4) + (PI / 16))

    createCubeVisual()
    
    
    
    # *************************************************************************************************
    
    
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
    # these functions handle solving the cube
    
    
def cubeNotSolved():
    if Cube == SolvedCube and block == SolvedBlock:
        return False
    else:
        return True


    # *************************************************************************************************
    
    
def compareBlocks(x, y, z):
    if Cube[x][y][z] == solvedCube[x][y][z]:
        if Cube[x][y][z].xFace == solvedCube[x][y][z].xFace and Cube[x][y][z].yFace == solvedCube[x][y][z].yFace and Cube[x][y][z].zFace == Cube[x][y][z].zFace:
            return True
        else:
            return False
    else:
        return False
    
    
    # *************************************************************************************************
    
def solveCube():
    if cross_Not_Solved():
        solve_Cross()
    
    elif f2l_Not_Solved():
        solve_f2l()
    
    elif OLL_Not_Solved():
        solve_OLL()
    
    elif PLL_Not_Solved():
        solve_PLL
        
    
    # *************************************************************************************************
    
def cross_Not_Solved():
    for y in range(0, 2):
        if compare(1, y, 0) != True:
            return False
    for x in range(0, 2):
        if compare(x, 1, 0) != True:
            return False
    return True
        
    
    
    # *************************************************************************************************
    
    
def solve_Cross():
    pass
    
    
    # *************************************************************************************************
    
    
def f2l_Not_Solved():
    pass
    
    
    # *************************************************************************************************
    
    
def solve_f2l():
    pass
    
    
    # *************************************************************************************************
    
    
def OLL_Not_Solved():
    pass
    
    
    # *************************************************************************************************
    
    
def solve_OLL():
    pass
    
    
    # *************************************************************************************************
    
    
def PLL_Not_Solved():
    pass
    
    
    # *************************************************************************************************
    
    
def solve_PLL():
    pass
    
    
    # *************************************************************************************************
    
    
    
    
    
    
    
    
    # *************************************************************************************************
    
    
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
        if cubeNotSolved():
            solveCube()
    elif key == 'r': # single moves
        R()
    elif key == 'R':
        R_()
    elif key == 'L':
        L_()
    elif key == 'l':
        L()
    elif key == 'f':
        F()
    elif key == 'F':
        F_()
    elif key == 'b':
        B()
    elif key == 'B':
        B_()
    elif key == 'u':
        U()
    elif key == 'U':
        U_()
    elif key == 'd':
        D()
    elif key == 'D':
        D_()
    elif key == 'm': # middle moves
        M()
    elif key == 'M':
        M_()
    elif key == 's':
        S()
    elif key == 'S':
        S_()
    elif key == 'e':
        E()
    elif key == 'E':
        E_()
    elif key == 'x': # rotations
        X()
    elif key == 'X':
        X_()
    elif key == 'y':
        Y()
    elif key == 'Y':
        Y_()
    elif key == 'z':
        Z()
    elif key == 'Z':
        Z_()
    elif key == ' ':
        applyScramble()


    # *************************************************************************************************
    
    
def applyScramble():
    sk = scramble()
    for move in sk:
        if move == 'R':
            R()
        elif move == 'R_':
            R_()
        elif move == 'L_':
            L_()
        elif move == 'L':
            L()
        elif move == 'F':
            F()
        elif move == 'F_':
            F_()
        elif move == 'B':
            B()
        elif move == 'B_':
            B_()
        elif move == 'U':
            U()
        elif move == 'U_':
            U_()
            
    
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # *************************************************************************************************
    # these functions handle turning the cube 


def R(): 
    global Cube
    
    
    # edges
    subs               = Cube[2][0][1]
    Cube[2][0][1]      = Cube[2][1][0]
    Cube[2][1][0]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[2][1][2]
    Cube[2][1][2]      = subs

    # corners
    subs               = Cube[2][0][0]
    Cube[2][0][0]      = Cube[2][2][0]
    Cube[2][2][0]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[2][0][2]
    Cube[2][0][2]      = subs

    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[2][yPos][zPos].yFace
            Cube[2][yPos][zPos].yFace = Cube[2][yPos][zPos].zFace
            Cube[2][yPos][zPos].zFace = subs
                           
          
  # *************************************************************************************************  
  
  
def R_(): 
    global Cube
    
    # edges
    subs               = Cube[2][0][1]
    Cube[2][0][1]      = Cube[2][1][2]
    Cube[2][1][2]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[2][1][0]
    Cube[2][1][0]      = subs

    # corners
    subs               = Cube[2][0][0]
    Cube[2][0][0]      = Cube[2][0][2]
    Cube[2][0][2]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[2][2][0]
    Cube[2][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[2][yPos][zPos].yFace
            Cube[2][yPos][zPos].yFace = Cube[2][yPos][zPos].zFace
            Cube[2][yPos][zPos].zFace = subs
    
    
    # *************************************************************************************************
  
  
def R2():
    R()
    R()  
  
  
    # *************************************************************************************************  
  
  
def L(): 
    global Cube
    
    # edges
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[0][1][2]
    Cube[0][1][2]      = Cube[0][2][1]
    Cube[0][2][1]      = Cube[0][1][0]
    Cube[0][1][0]      = subs

    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[0][0][2]
    Cube[0][0][2]      = Cube[0][2][2]
    Cube[0][2][2]      = Cube[0][2][0]
    Cube[0][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[0][yPos][zPos].yFace
            Cube[0][yPos][zPos].yFace = Cube[0][yPos][zPos].zFace
            Cube[0][yPos][zPos].zFace = subs
    
  
  # *************************************************************************************************  
  
  
def L_(): 
    global Cube
    
    # edges
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[0][1][0]
    Cube[0][1][0]      = Cube[0][2][1]
    Cube[0][2][1]      = Cube[0][1][2]
    Cube[0][1][2]      = subs

    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[0][2][0]
    Cube[0][2][0]      = Cube[0][2][2]
    Cube[0][2][2]      = Cube[0][0][2]
    Cube[0][0][2]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[0][yPos][zPos].yFace
            Cube[0][yPos][zPos].yFace = Cube[0][yPos][zPos].zFace
            Cube[0][yPos][zPos].zFace = subs
        
        
    # *************************************************************************************************  
  
  
def L2():
    L()
    L()  
  
  
    # *************************************************************************************************


def F(): 
    global Cube
    
    # edges
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[1][0][0]
    Cube[1][0][0]      = Cube[2][0][1]
    Cube[2][0][1]      = Cube[1][0][2]
    Cube[1][0][2]      = subs

    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[2][0][0]
    Cube[2][0][0]      = Cube[2][0][2]
    Cube[2][0][2]      = Cube[0][0][2]
    Cube[0][0][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][0][zPos].xFace
            Cube[xPos][0][zPos].xFace = Cube[xPos][0][zPos].zFace
            Cube[xPos][0][zPos].zFace = subs
        
        
        # *************************************************************************************************  
  
  
def F_(): 
    global Cube
    
    # edges
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[1][0][2]
    Cube[1][0][2]      = Cube[2][0][1]
    Cube[2][0][1]      = Cube[1][0][0]
    Cube[1][0][0]      = subs

    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[0][0][2]
    Cube[0][0][2]      = Cube[2][0][2]
    Cube[2][0][2]      = Cube[2][0][0]
    Cube[2][0][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][0][zPos].xFace
            Cube[xPos][0][zPos].xFace = Cube[xPos][0][zPos].zFace
            Cube[xPos][0][zPos].zFace = subs
     
        
    # *************************************************************************************************


def F2():
    F()
    F()  
  
  
    # *************************************************************************************************
    
   
def B(): 
    global Cube

    # edges
    subs               = Cube[0][2][1]
    Cube[0][2][1]      = Cube[1][2][2]
    Cube[1][2][2]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[1][2][0]
    Cube[1][2][0]      = subs
    
    # corners
    subs               = Cube[0][2][0]
    Cube[0][2][0]      = Cube[0][2][2]
    Cube[0][2][2]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[2][2][0]
    Cube[2][2][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][2][zPos].xFace
            Cube[xPos][2][zPos].xFace = Cube[xPos][2][zPos].zFace
            Cube[xPos][2][zPos].zFace = subs
    
        
    # *************************************************************************************************
    
    
def B_(): 
    global Cube

    # edges
    subs               = Cube[0][2][1]
    Cube[0][2][1]      = Cube[1][2][0]
    Cube[1][2][0]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[1][2][2]
    Cube[1][2][2]      = subs
    
    # corners
    subs               = Cube[0][2][0]
    Cube[0][2][0]      = Cube[2][2][0]
    Cube[2][2][0]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[0][2][2]
    Cube[0][2][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][2][zPos].xFace
            Cube[xPos][2][zPos].xFace = Cube[xPos][2][zPos].zFace
            Cube[xPos][2][zPos].zFace = subs
    
        
    # *************************************************************************************************
    
    
def B2():
    B()
    B()
    
    
    # *************************************************************************************************
    
    
def U(): 
    global Cube

    # edges
    subs               = Cube[1][0][2]
    Cube[1][0][2]      = Cube[2][1][2]
    Cube[2][1][2]      = Cube[1][2][2]
    Cube[1][2][2]      = Cube[0][1][2]
    Cube[0][1][2]      = subs
    
    # corners
    subs               = Cube[0][0][2]
    Cube[0][0][2]      = Cube[2][0][2]
    Cube[2][0][2]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[0][2][2]
    Cube[0][2][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][2].xFace
            Cube[xPos][yPos][2].xFace = Cube[xPos][yPos][2].yFace
            Cube[xPos][yPos][2].yFace = subs
        
        
    # *************************************************************************************************
    
    
def U_():
    global Cube

    # edges
    subs               = Cube[1][0][2]
    Cube[1][0][2]      = Cube[0][1][2]
    Cube[0][1][2]      = Cube[1][2][2]
    Cube[1][2][2]      = Cube[2][1][2]
    Cube[2][1][2]      = subs
    
    # corners
    subs               = Cube[0][0][2]
    Cube[0][0][2]      = Cube[0][2][2]
    Cube[0][2][2]      = Cube[2][2][2]
    Cube[2][2][2]      = Cube[2][0][2]
    Cube[2][0][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][2].xFace
            Cube[xPos][yPos][2].xFace = Cube[xPos][yPos][2].yFace
            Cube[xPos][yPos][2].yFace = subs
        
        
# *************************************************************************************************


def U2():
    U()
    U()
    
    
# *************************************************************************************************


def D(): 
    global Cube

    # edges
    subs               = Cube[1][0][0]
    Cube[1][0][0]      = Cube[0][1][0]
    Cube[0][1][0]      = Cube[1][2][0]
    Cube[1][2][0]      = Cube[2][1][0]
    Cube[2][1][0]      = subs
    
    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[0][2][0]
    Cube[0][2][0]      = Cube[2][2][0]
    Cube[2][2][0]      = Cube[2][0][0]
    Cube[2][0][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][0].xFace
            Cube[xPos][yPos][0].xFace = Cube[xPos][yPos][0].yFace
            Cube[xPos][yPos][0].yFace = subs
        
        
# *************************************************************************************************


def D_(): 
    global Cube

    # edges
    subs               = Cube[1][0][0]
    Cube[1][0][0]      = Cube[2][1][0]
    Cube[2][1][0]      = Cube[1][2][0]
    Cube[1][2][0]      = Cube[0][1][0]
    Cube[0][1][0]      = subs
    
    # corners
    subs               = Cube[0][0][0]
    Cube[0][0][0]      = Cube[2][0][0]
    Cube[2][0][0]      = Cube[2][2][0]
    Cube[2][2][0]      = Cube[0][2][0]
    Cube[0][2][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][0].xFace
            Cube[xPos][yPos][0].xFace = Cube[xPos][yPos][0].yFace
            Cube[xPos][yPos][0].yFace = subs
        
        
    # *************************************************************************************************
    
    
def D2():
    D()
    D()
    
    
    # *************************************************************************************************


def M(): 
    global Cube
    
    # edges
    subs               = Cube[1][0][1]
    Cube[1][0][1]      = Cube[1][1][2]
    Cube[1][1][2]      = Cube[1][2][1]
    Cube[1][2][1]      = Cube[1][1][0]
    Cube[1][1][0]      = subs

    # corners
    subs               = Cube[1][0][0]
    Cube[1][0][0]      = Cube[1][0][2]
    Cube[1][0][2]      = Cube[1][2][2]
    Cube[1][2][2]      = Cube[1][2][0]
    Cube[1][2][0]      = subs
    
    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[1][yPos][zPos].yFace
            Cube[1][yPos][zPos].yFace = Cube[1][yPos][zPos].zFace
            Cube[1][yPos][zPos].zFace = subs
    
    
    # *************************************************************************************************


def M_(): 
    global Cube
    
    
    # edges
    subs               = Cube[1][0][1]
    Cube[1][0][1]      = Cube[1][1][0]
    Cube[1][1][0]      = Cube[1][2][1]
    Cube[1][2][1]      = Cube[1][1][2]
    Cube[1][1][2]      = subs

    # corners
    subs               = Cube[1][0][0]
    Cube[1][0][0]      = Cube[1][2][0]
    Cube[1][2][0]      = Cube[1][2][2]
    Cube[1][2][2]      = Cube[1][0][2]
    Cube[1][0][2]      = subs

    # orientation
    for yPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[1][yPos][zPos].yFace
            Cube[1][yPos][zPos].yFace = Cube[1][yPos][zPos].zFace
            Cube[1][yPos][zPos].zFace = subs
                          
          
  # *************************************************************************************************  


def M2():
    M()
    M()


    # *************************************************************************************************


def E(): 
    global Cube

    # edges
    subs               = Cube[1][0][1]
    Cube[1][0][1]      = Cube[0][1][1]
    Cube[0][1][1]      = Cube[1][2][1]
    Cube[1][2][1]      = Cube[2][1][1]
    Cube[2][1][1]      = subs
    
    # corners
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[0][2][1]
    Cube[0][2][1]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[2][0][1]
    Cube[2][0][1]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][1].xFace
            Cube[xPos][yPos][1].xFace = Cube[xPos][yPos][1].yFace
            Cube[xPos][yPos][1].yFace = subs


    # *************************************************************************************************


def E_(): 
    global Cube

    # edges
    subs               = Cube[1][0][1]
    Cube[1][0][1]      = Cube[2][1][1]
    Cube[2][1][1]      = Cube[1][2][1]
    Cube[1][2][1]      = Cube[0][1][1]
    Cube[0][1][1]      = subs
    
    # corners
    subs               = Cube[0][0][1]
    Cube[0][0][1]      = Cube[2][0][1]
    Cube[2][0][1]      = Cube[2][2][1]
    Cube[2][2][1]      = Cube[0][2][1]
    Cube[0][2][1]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for yPos in range(0, 3):
            subs = Cube[xPos][yPos][1].xFace
            Cube[xPos][yPos][1].xFace = Cube[xPos][yPos][1].yFace
            Cube[xPos][yPos][1].yFace = subs
        
        
    # *************************************************************************************************


def E2():
    E()
    E()


    # *************************************************************************************************


def S(): 
    global Cube
    
    # edges
    subs               = Cube[0][1][1]
    Cube[0][1][1]      = Cube[1][1][0]
    Cube[1][1][0]      = Cube[2][1][1]
    Cube[2][1][1]      = Cube[1][1][2]
    Cube[1][1][2]      = subs

    # corners
    subs               = Cube[0][1][0]
    Cube[0][1][0]      = Cube[2][1][0]
    Cube[2][1][0]      = Cube[2][1][2]
    Cube[2][1][2]      = Cube[0][1][2]
    Cube[0][1][2]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][1][zPos].xFace
            Cube[xPos][1][zPos].xFace = Cube[xPos][1][zPos].zFace
            Cube[xPos][1][zPos].zFace = subs
        
        
        # *************************************************************************************************  
  
  
def S_(): 
    global Cube
    
    # edges
    subs               = Cube[0][1][1]
    Cube[0][1][1]      = Cube[1][1][2]
    Cube[1][1][2]      = Cube[2][1][1]
    Cube[2][1][1]      = Cube[1][1][0]
    Cube[1][1][0]      = subs

    # corners
    subs               = Cube[0][1][0]
    Cube[0][1][0]      = Cube[0][1][2]
    Cube[0][1][2]      = Cube[2][1][2]
    Cube[2][1][2]      = Cube[2][1][0]
    Cube[2][1][0]      = subs
    
    # orientation
    for xPos in range(0, 3):
        for zPos in range(0, 3):
            subs = Cube[xPos][1][zPos].xFace
            Cube[xPos][1][zPos].xFace = Cube[xPos][1][zPos].zFace
            Cube[xPos][1][zPos].zFace = subs
     
        
    # *************************************************************************************************


def S2():
    S()
    S()  
  
  
    # *************************************************************************************************


def r(): 
    R()
    M_()


    # *************************************************************************************************


def r_(): 
    R_()
    M()


    # *************************************************************************************************

    
def r2(): 
    r()
    r()
    

    # *************************************************************************************************
    
    
def l(): 
    L()
    M()


    # *************************************************************************************************


def l_(): 
    L_()
    M_()


    # *************************************************************************************************

    
def l2(): 
    l()
    l()


    # *************************************************************************************************
    

def u(): 
    U()
    E_()


    # *************************************************************************************************


def u_(): 
    U_()
    E()


    # *************************************************************************************************

    
def u2(): 
    u()
    u()


    # *************************************************************************************************
    

def d(): 
    D()
    E()


    # *************************************************************************************************


def d_(): 
    D_()
    E_()


    # *************************************************************************************************

    
def d2(): 
    d()
    d()


    # *************************************************************************************************

    
def f(): 
    F()
    S()


    # *************************************************************************************************


def f_(): 
    F_()
    S_()


    # *************************************************************************************************

    
def f2(): 
    f()
    f()


    # *************************************************************************************************
    
  
def b(): 
    B()
    S_()


    # *************************************************************************************************
    

def b_(): 
    B_()
    S()


    # *************************************************************************************************


def b2(): 
    b()
    b()

    # *************************************************************************************************

    
def X(): 
    R()
    l_()


    # *************************************************************************************************


def X_(): 
    R_()
    l()


    # *************************************************************************************************

    
def X2(): 
    X()
    X()


    # *************************************************************************************************
    

def Y(): 
    U()
    d_()


    # *************************************************************************************************


def Y_(): 
    U_()
    d()


    # *************************************************************************************************

    
def Y2(): 
    Y()
    Y()


    # *************************************************************************************************
    

def Z(): 
    F()
    b_()


    # *************************************************************************************************


def Z_(): 
    F_()
    b()


    # *************************************************************************************************
    
    
def Z2(): 
    Z()
    Z()


    # *************************************************************************************************

    
