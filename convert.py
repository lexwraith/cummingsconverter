import random

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

def randomSpacing(words,chance=percentage):
    """
    Cummings had a thing for "cubism" poetry and would often randomly
    remove spacings between words. 
    """
    #Making sure percentage is in range of 0-100
    if 0 < percentage < 1:
        percentage *= 100
    
    #The actual removing of spaces.
    

def randomNewLine(words):
    """
    """
    pass

def randomTabbing(words):
    """
    Cummings also would randomize the tabbing.
    """

def randomCapitalization(words):
    """
    Determines 
    """
    pass

def main(filename):
    words = openFile("sample.txt")
    

if __name__ == "__main__":
    """
    Test stuff, delete me when done.
    """
    main("sample.txt")
    
            
