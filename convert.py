from random import randint
from pprint import pprint

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
    chunked together. If it is, then the 0th + 1st is now the 0th,
    and the problem repeats. But in Python, it's just as
    memory intensive, as there is no tail recursion optimization.
    """
    chunks = [words[0]]
    words = words[1:]
    while len(words) > 0:
        if randint(1,99)<percentage:
            chunks[-1] = "".join([chunks[-1],words[0]])
        else:
            chunks.append(words[0])
        words = words[1:]
    return chunks

def randomNewLine(words,percentage=50):
    """
    Makes chunks into coherent (haha) lines with a newline character
    at the end.
    
    IDEA:This is remarkably similar to randomChunking...is there a way
    to make this better?
    """
    lines = [words[0]]
    words = words[1:]
    while len(words) > 0:
        if randint(1,99)<percentage:
            lines[-1] = " ".join([lines[-1],words[0]])
        else:
            lines.append(words[0] + "\n")
        words = words[1:]
    return lines

def randomTabbing(poem,percentageLine=20,percentageTabs=30,colGuard=80):
    """
    Cummings also would randomize the tabbing.
    percentageLine is the chance of a line being altered
    percentageTabs is the chance of a line having more than one tab
    colGuard is the cutoff point (if a line exceeds 79, no more tabs)
    """
    newPoem = []
    for line in poem:
        roll = randint(1,99)
        if randint(1,99) < percentageLine:
            tabBuffer = "\t"
            while len(tabBuffer) * 4 + len(line) < 79:
                roll = randint(1,99)
                if roll < percentageTabs:
                    tabBuffer = tabBuffer + "\t"
                else:
                    newPoem.append("".join([tabBuffer,line]))
                    break
        else:
            newPoem.append(line)
    return newPoem

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
        
def main(filein,fileout):
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
    words = openFile(filein)
    words = randomCapitalization(words,10)
    words = randomCase(words,20,20)
    words = randomChunking(words,20)
    words = randomNewLine(words,80)
    words = randomTabbing(words,80)
    
    with open(fileout,"w") as f:
        for elem in words:
            f.write(elem)
    for elem in words:
        print elem
    

if __name__ == "__main__":
    """
    Test stuff, delete me when done.
    """
    main("sample.txt","poem.txt")
    
            
