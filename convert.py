from random import randint

def openFile(filename):
    """
    Collects all the words and symbols within a text file while
    maintaining their order.
    """
    with open(filename) as f:
        words = []
        for line in f:
            for elem in line.strip().split():
                if elem[-1] in ".!,;:?":
                    words.append(elem[:-1])
                    words.append(elem[-1])
                else:
                    words.append(elem)
        return words

def randomChunking(words,percentage=0):
    """
    Randomly removes spaces between words.
    IT TURNS THE WORD ARRAY INTO A WORDS LIST,
    I.E. A LIST OF CHUNKS.
    
    TODO: Kind of memory intensive because of the rapid
    list re-copying. Need to find a better way to do this.
    
    IDEA: Couldn't this be done recursively? The sub-problem
    is whether or not the 0th word and the 1st word should be
    chunked together.
    """
    chunks = []
    while len(words) > 0:
        roll = randint(1,99)
        if 

def randomNewLine(words):
    """
    """
    pass

def randomTabbing(words):
    """
    Cummings also would randomize the tabbing.
    """

def randomCapitalization(words,percentage=0):
    """
    Capitalizes the first letter or not.
    """
    newWords = []
    for elem in words:
        if randint(1,99) < percentage and elem not in ".!,;:?":
            newWords.append(elem.capitalize())
        else:
            newWords.append(elem.lower())
    return newWords
        
def randomCase(words,percentageWord=0,percentageLetter=0):
    """
    Random capitalization of all letters within the word list.
    """
    newWords = []
    for word in words:
        if  randint(1,99) < percentageWord:
            temp = [letter.upper() if randint(1,99) < percentageLetter else letter for letter in word]
            newWords.append("".join(temp))
        else:
            newWords.append(word)
    return newWords
        
def main(filename):
    """
    Flow of operations:
    1. Open file and get word list
    2. Random capitalization of first letter
    3. Random capitalization of rest of word
    4. "Chunking" words together
    5. Randomizing what chunks are independent lines
    6. Randomizing tabbing of each line
    7. Output into screen or file
    """
    words = openFile("sample.txt")
    words = randomCapitalization(words,10)
    words = randomCase(words,20,20)
    words = randomChunk(words,20)
    print words
    

if __name__ == "__main__":
    """
    Test stuff, delete me when done.
    """
    main("sample.txt")
    
            
