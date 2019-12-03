import random
import string
import numpy as np
import requests

# # # get random string and its type is str
# ch = ''.join(random.sample(string.ascii_uppercase, 9))
# print ch
# print type(ch)

# # # print in grid format

# # # shuffle string output
# shuffledStr = ''.join(random.sample(ch, len(ch)))
# print shuffledStr

# # word should have min 3 chars
# s = raw_input("Enter word: ")
# if (len(s) < 3):
#     print "word should have min 3 chars"

# # using wordnik.com , check if entered word is valid and if valid then score it
# # score also will come from wordnik.com.
# # https://developer.wordnik.com/docs#!/word/getScrabbleScore

# import requests
# url = "https://api.wordnik.com/v4/word.json/{}/scrabbleScore?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5".format(s)
# header = {"content-type": "application/json"}
# response = requests.get(url, headers=header)
# print response.json()
# print response.status_code

score = 0
used_words = []
letters = ""
innerList = []
Samplearray = """
 %s | %s | %s
 ---------
 %s | %s | %s
 ---------
 %s | %s | %s
 """ 


# def random.shuffle(self, gameLetters):
#     letters = ''.join(random.sample(gameLetters, len(gameLetters)))
#     return letters

def select_letters():
    print("Welcome to word find.")
    print("Come up with as many words as possible from the letters below!\n")
    createRandomLetters(innerList)
    while True:
        print("Score: {}. Your letters are: \n".format(score))
        
        userInput = raw_input("Enter a word, [s]huffle letters, [l]ist words, or [e]nd game: ")
        userInput = userInput.upper()
        if userInput == "S":
            # Shuffling the letters
            print("Shuffling letters...")
            print("Score: {}. Your letters are: \n".format(score))
            random.shuffle(innerList)
            print(Samplearray % tuple(innerList))
            userInput = raw_input("Enter a word, [s]huffle letters, [l]ist words, or [e]nd game: ")
            userInput = userInput.upper()
        elif userInput == "L":
            # list the words
            pass

        elif userInput == "E":
            # end the game
            print("Ending game...")
            break

        elif len(userInput) < 3:
            print("Please input minimum three char word..")

        elif len(userInput) >= 3:
            print("i m here")
            # check if word is recognised
            url = "https://api.wordnik.com/v4/word.json/{}/scrabbleScore?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5".format(userInput)
            header = {"content-type": "application/json"}
            response = requests.get(url, headers=header)
            if response.status_code == 200:
                used_words.append(userInput)
                resDict = response.json()
                print(resDict)
            else:
                print(response.json())
                print("not reco")

def createRandomLetters(innerList):
    for i in range(9):
        letter = random.choice(string.ascii_letters).upper()
        innerList.append(letter)
    print(Samplearray % tuple(innerList))

# def showDataInGrid(innerList):
#     if not innerList:
#         for i in range(9):
#             letter = random.choice(string.ascii_letters).upper()
#             innerList.append(letter)
    
#     matrix = np.array(innerList)
#     matrix = matrix.reshape((3,3))
#     for i in range(3):
#         for j in range(3):
#             print(matrix[i][j])
#         print('\n')

if __name__ == "__main__":
    select_letters()
