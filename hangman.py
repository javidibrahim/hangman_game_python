import random

#input validation function
def validateChar(character):
    while ord(character) < 65 or ord(character)>90:
        character = input("Enter a character between A and Z all capital: ")
    return character
  
def printTheWord(word):
    for i in word:
        print(i, end=" ")

def combine(array,letter):
  array += letter
  return array

#how many words in the list
seedSize = 10
lives = 3

seed = ["HELLO", "SALAM", "WORD", "PICTURE", "BOOK", "PHONE", "GLASS", "BOTTLE", "LAPTOP", "ADAPTER"]
#random index to pick a number
randWordIndex = random.randint(0, seedSize-1)

#pick a random word
gameWord = seed[randWordIndex]
#create an empty array of chars same as gameword size
emptyWord = ['_']*len(gameWord)


#display empty array 
for i in emptyWord:
    print(i, end=" ")


while(lives != 0 or emptyWord == gameWord):
    #ask for user to enter a char
    character = input("\nEnter a character: ")
  
    character = validateChar(character)
    
    matched = False
    for i in range(len(gameWord)):
        if gameWord[i] == character:
            emptyWord[i] = character
            matched = True

    if matched == False:
        lives-=1

    new = ""
    notfull = False
    for i in range(len(emptyWord)):
      if emptyWord[i] == '_':
        notfull = True

    if(notfull == False):
      for i in emptyWord:
          new = combine(new, i)
  
    if(new == gameWord):
      print(f"You won! --- > {new}")
    else:
      if(lives == 0):
        print("\nYou Lost!")v
        print(gameWord)
      else:
        printTheWord(emptyWord)
  




