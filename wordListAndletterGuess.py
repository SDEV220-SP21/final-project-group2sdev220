# def createCanvas():
    #text box field(blah blah , command = letterguess())
#def chooseWord():
    #get word
    #wordArray = []
    #asteriskArray = []

def getWordList():
    file = open('wordList.txt', 'r')
    wordArray = []
    i = file
    for words in i.read().split():
        wordArray.append(words)
    
            
        
    
    

def letterGuess(textBox, wordArray, asteriskArray):
    found = False
    countGuess = 0
    userInput = textBox.get()
    for el in wordArray:
        if userInput == el:
            found = True
        else:
            countGuess += 1
    if found == True:
        asteriskArray[countGuess] = textBox.get()
    else:
        missedGuesses += 1
        drawHouse()


            
    
        


    
    
    
    
    
            
