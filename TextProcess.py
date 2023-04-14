class Token:
    def __init__(token, word, frequency):
        token.word = word
        token.frequency = frequency


def tokenize(TextFilePath):
    # returns a list of tokens from the file #
    tokens = TextFilePath.split(); 
    # make a new list 'tokens' that will have each word of TextFilePath in it through use of split() #
    return tokens;

def computeWordFrequencies(tokens):
    wordFreqMap = {}
    # initialize a map
    for word in tokens:
        if word in tokens:
            wordFreqMap[word] += 1
            # if the map contains the word, increment the value that the word is mapped to by one
        else: 
            wordFreqMap[word] = 1
    return wordFreqMap        
            # if the map doesn't contain the word, assign the value 1 to that word

def print(wordFreqMap):
    for key, value in wordFreqMap.items():
        print(key, " : ", value)
    # for every key in the map, print out the key and value
