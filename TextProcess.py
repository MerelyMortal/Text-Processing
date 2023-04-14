import re
import string

class Token:
    def __init__(token, word, frequency):
        token.word = word
        token.frequency = frequency


def tokenize(TextFilePath):
    # returns a list of tokens from the file #
    tokens = TextFilePath.split(); 
    
    # make a new list 'tokens' that will have each word of TextFilePath in it through use of split() #
    
