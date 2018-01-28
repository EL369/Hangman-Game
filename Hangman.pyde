import random
  
def setup():
    global post, hangman, Qmark
    global letters, word, dictionary, keyboardBound, hangmanParts, keyboardvalue, alphabet
    global squaresize, numrow, numcolumn, gridw, gridh, showSquareX, showSquareY, startSquareX, startSquareY
    global hintclicked, hintcounter, tries, hintline, letterclicked, validletter, letterlocation
    global word, wordnum, wordlength,wordonscreen
    global gamedictionary, gdkey, dfilename, lbfilename
    global mode, lettercolour, gamecounter
    global playerscore, playername, lb, leaderboard, bg1, rulescreen, losescreen
    global running, loseword, xloc, x, post, winword, yloc, yloc2
    global imglocation, modes, playername, begin, leaderboardimg, rule, title, deadman, playername, lblineLocation, lb, x
    
    startSquareX = 200
    startSquareY = 600
    showSquareX = startSquareX
    showSquareY = startSquareY
    squaresize = 50
    numrow = 2
    numcolumn = 13
    keyboardBound = []
    keyboardvalue = []
    keyIndex = 0
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lettercolour = []

    mode = "initsetup"
    alphabet = {}
    currentword = 0
    tries = 0
    gamecounter = 0
    leaderboard = []

    letterclicked = False
    letterlocation = []
    
    hangmanParts = [[230,205,150,95], [295,305,20,133], [230,305,65,95], [315,305,65,95], [230,440,70,90], [309,440,70,90]]
    imglocation = [ [[400, 360], [600, 560]], [[170, 400],[320, 550]], [[680, 400], [830, 550]] ]
    modes = ["gamesetup", "leaderboard", "rules"]
    
    
    hintclicked = False
    hintcounter = 0
    hintline = ""
    
    gamedictionary = {}
    word = ""
    wordnum = 0
    wordlength = 0
    wordonscreen = ""

    playerscore = 0
    playername = ""
    
    size(1000,800)
    bg1 = loadImage ("background.jpg")
    losescreen = loadImage ("lost.jpg")

    
    title = loadImage ("title.png")
    begin = loadImage ("begin.png")
    leaderboardimg = loadImage ("leader.png")
    rule = loadImage ("rule.png")
    deadman = loadImage ("dead.png")
    rulescreen = loadImage("rules.png")
    
    running = loadImage ("people.png") 
    loseword = loadImage ("loseword.png")
    winword = loadImage ("winword.png")
    
    post = loadImage ("Post.png") # original size 300, 470
    hangman = loadImage("StickFigure.png") # original size( 750, 1600)
    Qmark = loadImage ("QuestionMark.png")
    
    
    
    xloc = 230
    x = 0
    yloc = -100
    yloc2 = -100
    
    dfilename = "info.txt"
    lbfilename = "leaderboard.txt"
    
#FUNCTIONS

def readFileToDictionary(filename):
    file = open(filename)
    text = file.readlines()
    gdkey = -1
    for line in text:
        line = line.strip()
        row = ""
        for c in line:
            row = row + c
        temprow = row.split(",")
        gdkey = gdkey + 1
        gamedictionary[ gdkey ] = ( temprow[0], temprow[ 1:4 ], int( temprow[4] ) )
    return gamedictionary

def readFileToList(filename):
    file = open(filename)
    listfromfile = []
    text = file.readlines()
    
    for line in text:
        line = line.strip()
        row = ""
        for c in line:
            row = row + c
        
        addrow = row.split(",")
        listfromfile.append( addrow )
    return ( listfromfile )

def AppendToFile(filename, data):
    file = open(filename, "a")
    file.write(data + "\n")
    file.close
    
def MakeGrid(sqsize, row, column, sqX, sqY):
    # gets the size of each square and how many rows and columns
    # calculates the coordinate of each square
    originalsqX = sqX
    allBoundaries = []
    for i in range(row):
        for j in range (column): 
            upperLeft =  [ sqX, sqY ]
            lowerRight = [ sqX + sqsize, sqY + sqsize ]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            sqX = sqX + sqsize
            
        sqY = sqY + sqsize
        sqX = originalsqX 
    return (allBoundaries)

def AddToDictionary(data, dictionary):
    # this funciton takes the data needed to be stored into the dictionary and the dictionary
    # the function then checks if the item is already there, if its not there, it will add the item to the dictionary
    # does not return anything
    if not ( data in dictionary ):
        print ( "This is the character you entered", data )
        dictionary[ data ] = True
    else:
        print ( "This character has been taken already", data )
        
        
def sort2D(datalist, numitems, whichcolumn ):
    for i in range (1, numitems):
        swap = False
        for j in range (numitems - i):
            if datalist[j][whichcolumn] < datalist[j+1][whichcolumn]:
                temp = datalist[j]
                datalist[j] = datalist [j+1]
                datalist [j+1] = temp
                swap = True
        if not swap :
            break
    return (datalist)

def LetterinString (letter, string):
    # this function gets the letter and word/string
    # checks to see if the letter is in the string using the 'in' command
    # returns if the letter is in the string, and the locations of that letter in a list
    num = 0
    location = []
    stringlength = len(string)
    itsthere = False
    if letter in string:
        itsthere = True
        for i in range (stringlength):
            if string[i] == letter:
                location.append (i)
    return (location, itsthere)

def replaceletters (letter, string , location ):
    numofletters = len(location)
    for i in range (numofletters):
        string = string [:(location[i])] + letter + string [location[i]+1:]

    return (string)


def draw(): 
    global post, hangman, Qmark, running, loseword, xloc, letternum, post, winword, yloc, yloc2
    global letters, word, dictionary, keyboardBound, hangmanParts, keyboardvalue, alphabet
    global squaresize, numrow, numcolumn, gridw, gridh, showSquareX, showSquareY, startSquareX, startSquareY
    global hintclicked, hintcounter, tries, hintline, letterclicked, validletter, letterlocation
    global word, wordnum, wordlength, wordonscreen
    global gamedictionary, gdkey, dfilename, lbfilename
    global mode, lettercolour, x, gamecounter, bg1, rulescreen, losescreen
    global playerscore, playername, lb, leaderboard, file
    global  begin, leaderboardimgshe, rule, title, deadman, playername, lblineLocation, lb, x


    if mode == "initsetup" : 
        gamecounter = 0
        gamedictionary = readFileToDictionary(dfilename)
        leaderboard = readFileToList(lbfilename)
        print leaderboard  
        for i in range (len(leaderboard)):  # this for loop chagnes the scores from string into an integer
            leaderboard [i][1] = int(leaderboard[i][1])
        leaderboard = sort2D(leaderboard, len(leaderboard) , 1) # sorts by score
        print leaderboard
        
        mode = "titlescreen"
        
    if mode == "titlescreen" :
        background(bg1)
        
        if yloc < 0:
            yloc = yloc + 5
        image(deadman, 370, yloc, 45, 200)
        image(title, 300, 20, 400, 200)
        image(begin, 400, 360, 200, 200)
        image(leaderboardimg, 170, 400, 150, 150)
        image(rule, 680, 400, 150, 150)
        fill(250)
        rect(400, 570, len(playername)*22, 40 )
        fill(0)
        textSize(40)
        text("Player:", 250, 600) 
        textSize (35)
        text (playername, 400, 600)
        
    if mode == "rules":
        image (rulescreen, 0, 0, 1000,800)
        text ("Press Q to go back", 540,740)
            
    if mode == "leaderboard":
        background(bg1)
        text("Current Leaderbaord Top 5", 100, 100)
        text ("Press Q to go back", 540,740)
        lblineLocation = 250
        for i in range (5):
            text (leaderboard[i][0], 100, lblineLocation)
            text (leaderboard[i][1], 300, lblineLocation)
            lblineLocation = lblineLocation + 50

    if mode == "gamesetup":
        (keyboardBound) = MakeGrid(squaresize, numrow, numcolumn, showSquareX, showSquareY)
        keyboardvalue = [True for i in range (numrow*numcolumn)]
        lettercolour = [0 for i in range (26)]
        wordnum = random.randint (0, len(gamedictionary)-1) # index to dictionary
        word = gamedictionary[wordnum][0].upper() # the actual word
        wordlength = gamedictionary[wordnum][2] # the length of the word/score
        wordonscreen = "_" * wordlength # word printed on the screen
        tries = 0
        print word, wordlength, wordonscreen
        xloc = 230
        x = 0
        yloc = -100
        yloc2 = -100
        mode = "play"

    

    if mode == "play":
        background(bg1)

        for i in range (numrow): 
            for j in range(numcolumn):
                fill(lettercolour[(i * numcolumn) + j])
                textSize(30)
                text (letters[ i*numcolumn+j ], showSquareX+15, showSquareY+40)
                noFill ()
                rect( showSquareX, showSquareY, squaresize, squaresize )
                showSquareX = showSquareX + squaresize
            showSquareX = startSquareX 
            showSquareY = showSquareY + squaresize        
        showSquareY = startSquareY
        
        if letterclicked:
            AddToDictionary(validletter, alphabet )
            lettercolour[letternum] = 200
            (letterlocation, letterthere ) = LetterinString( validletter, word)
            if not letterthere: 
                tries = tries + 1
            wordonscreen = replaceletters ( validletter, wordonscreen, letterlocation)
            letterclicked = False
        
        if hintclicked and (hintcounter <= 2): 
            tries = tries + 1
            hintline =("Hint: " + gamedictionary[wordnum][1][hintcounter])
            hintcounter = hintcounter + 1
            hintclicked = False
                    
        image(post, 50, 100, 300, 470)
        image(Qmark, startSquareX - 130, startSquareY, 90, 90)
        textSize(50)
        fill(0)
        text (wordonscreen, 450, 300)
        textSize(40)
        text(hintline, startSquareX, startSquareY + 150 ) 
        
        for i in range (tries):
            copy (hangman, hangmanParts[i][0]-230, hangmanParts[i][1]-205, hangmanParts[i][2], hangmanParts[i][3], hangmanParts[i][0], hangmanParts[i][1], hangmanParts[i][2], hangmanParts[i][3])
            
        if tries == 6:
            gamecounter = gamecounter +1
            mode = "lose"
            print gamecounter
            
        if wordonscreen == word: 
            gamecounter = gamecounter +1
            playerscore = playerscore + wordlength
            print gamecounter

            mode = "win"

    if mode == "win":
        background(bg1)
        
        fill(255)
        image(post, 50, 100, 300, 470)
        if xloc < 1000:
            xloc = xloc + 50
            x = x + 125
            copy(running, x, 0, 123, 155, xloc, 400, 125, 155)
            
        else:
            if yloc < 300:
                yloc = yloc + 20
            image(winword, 500, yloc, 300, 200)    
                    
    if mode == "lose":
        background (losescreen)
        if yloc2 < 300:
            yloc2 = yloc2 + 50
        image(loseword, 500, yloc2, 300, 200)
        
    if gamecounter == 5:
        output = playername + "," + str(playerscore)
        AppendToFile (lbfilename, output)
        mode = "initsetup" 
            
        
        
    
def mouseReleased():
    global hintclicked, startSquareX, startSquareY, mode, keyboardBound, numrow, numcolumn, keyboardvalue, letterclicked, validletter, letternum ,modes
    if mode == "play":
        if ((startSquareX - 130) <= mouseX <= (startSquareX - 130 +90)) and ((startSquareY) <= mouseY <= (startSquareY+90)):
            print (" i clicked the box")
            hintclicked = True
            print (hintclicked)
        
        for i in range(numrow * numcolumn): 
            if  keyboardBound[i][0][0] <= mouseX <= keyboardBound[i][1][0] and keyboardBound[i][0][1]  <= mouseY <= keyboardBound[i][1][1] and (keyboardvalue[i]): 
                letterclicked = True
                keyboardvalue [i]= False # keeps track of wheter the letter has been clicekd already
                validletter = chr(i + 65)
                letternum = ord(validletter) - 65
                print validletter, letternum
                
    if mode == "titlescreen":
        for j in range (len(imglocation)):            
            if (imglocation[j][0][0] <= mouseX <= imglocation[j][1][0]) and (imglocation[j][0][1] <= mouseY <= imglocation[j][1][1]):
                mode = modes[j]
                
    if mode == "rules":
        if (865 < mouseX < 943) and (690 < mouseY < 770):
            mode = "titlescreen"

        
        
def keyReleased():
    global keyboardvalue, alphabet, letterclicked, validletter, mode, letternum, playername
    if key == "q" and (mode == "rules" or mode == "leaderboard"):
        mode = "titlescreen"
    if (key == ENTER) and ((mode == "titlescreen")or(mode == "win") or (mode == "lose")):
        mode = "gamesetup"
    
    
    validletter = key
    if mode == "titlescreen": # the following statements 
        if validletter.isalnum():
            newkey =  str(key)
            playername = playername + newkey
        if (key == BACKSPACE):
            playername = playername[0 : len(playername)-1]



    if (validletter >= 'a')and (validletter <= 'z') and mode == "play":  
        validletter = validletter.upper()
        letterclicked = True
        letternum = ord(validletter) - 65
        print validletter, letternum