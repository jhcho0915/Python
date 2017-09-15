# p3.py: Word Puzzles
# Created by: Jae Cho
# E-mail: jhcho@email.wm.edu

# This project is about files,strings and procedures and allows the 
# user to choose a word game to play.

# The program calls the procedure that plays the game and returns to the menu
# for another choice.

# Find all words of a particular length containing just a single vowel that 
# does not have a particular letter in it. In the procedure for this puzzle, 
# your program will ask for the length of the words you are looking for and the
# letter that should be missing from eachar word. It will then find and print 
# the words that matchar this criteria.

# Find all words containing all of the letters of a particular word.
# In the procedure for this puzzle, the user will enter the word whose letters
# s/he is looking for. In addition, the user will enter a maximum length of 
# the words they want to see. The procedure will find and print the words that
# contain all the letters of the given word that are that length or less. 
# Note that if there are duplicate letters in the entered word, the found words
# must also contain the duplicated letters.

# Find all words that contain all but one of the letters of a string of unique
# characters. In the procedure for this puzzle, the user will enter the string
# and print all words containing all but any one of the letters of the string.

# When writing in script, there are four letters of the alphabet that cannot be 
# completed in one stroke: i, j, t and x. Find all words that use each of these 
# letters exactly once.

# Find all the palindromes of a particular length.


# Choice A
def findOneVowel(dataFile):
   '''This procedure for letter choice A looks for words that are a certain 
number of characters with only one vowel. Also a letter has been excluded'''

# Assign variables to input statements
   length = int(input("Please enter the word length: "))
   print (length)
   letter = input("Please enter the letter to exclude: ")
   print(letter,'\n')
   count= 0
   vowels = 'aeiou'

   for word in dataFile:              # For each word in dataFile
      word = word.strip().lower()     # Strips spaces and converts to lowercase
      if len(word) == length and letter not in word:
         word_count = 0         
         for char in word:            # For each character in the word
            if char in vowels:
               word_count +=1         # Add words with character in vowels
            
         if word_count == 1:          # If the word has only one vowel...
            count+= 1                 # Add to list
            print (word)

   if count== 0:
      print("There are no words that fit this criteria.")

# Choice B
def findWordsMax(dataFile):
   '''This procedure prompts the user to take in a word and finds words that 
contain all the letters of that word. It also asks for a maximum length of
the words included in our list'''

   term = input("Please enter word: ")
   print (term)
   length = input("Please enter the maximum word length: ")
   print(length,'\n')
   length = int(length)                # Convert to an integer
   count= 0

   for word in dataFile:
      word = word.strip().lower()
      if len(word) <= length:
         word_kept = word
         word_count = 0
         for char in term:
            if char in word:
               word = word.replace(char,"",1)
               word_count += 1

         if word_count == len(term):
            print (word_kept)
            count+= 1

   if count== 0:
      print("There are no words that fit this criteria.")

# Choice C
def findCharacters(dataFile):
   '''This procedure extracts a string of unique characters and looks for 
words that contain all but one letter of that string'''

   string = input("Please enter a string of unique characters: ")
   print (string + '\n')
   count= 0

   for word in dataFile:
      word = word.lower().strip()
      word_count = 0
      for char in string:
         if char in word:
            word_count += 1

      if word_count + 1 == len(string):
         print(word)
         count+= 1
         
   if count== 0:
      print("There are no words that fit this criteria.")

# Chioce D
def findijtx(dataFile):
   '''This procedure looks for words containing the letters i,j,t and x
no more than once'''

   ijtx = "ijtx"
   count= 0
  
   for word in dataFile:
      word = word.lower().strip()
      word_count = 0
      for char in ijtx:
         if word.word_count(char) == 1:
            word_count += 1

      if word_count == 4:
         print(word)
         count+= 1

   if count== 0:
      print("There are no words that fit this criteria.")

# Choice E
def findPalindrome(dataFile):
   '''This function prompts the user to look for palindromes of a particular 
length of the word'''

   length = input("Please enter the length of the palindromes: ")
   length = int(length + '\n')
   count= 0

   for word in dataFile:
      word = word.strip().lower()
      if word == word[::-1] and len(word) == length:
         print(word)
         count+= 1

   if count== 0:
      print("There are no words that fit this criteria.")
      
      
# Main program
print ("\nWord Puzzles")

# Open dictionary file containing word list
dataFile = open("dictionary.txt","r")
choice = ""

# Input the print menu options in a loop excpet for 'Q' or 'q'.
while choice != "q":
   print ("\nPlease choose a puzzle from the following options: \n")
   print ("a) Find words with only one vowel and excluding a specific letter")
   print ("b) Find words containing all the letters of another word with \
a maximum length")
   print ("c) Find words containing all characters but one of a given string")
   print ("d) Find words containing i, j, t and x one time each")
   print ("e) Find all the palindromes of a particular length")
   print ("q) Quit" + '\n')

# Ask the user which choice s/he would like to select
   choice = input("Choice: ")
   print (choice + '\n')
   choice = choice.lower()
   dataFile.seek(0)                        # Keeps the file open

# Return the choices to their respective functions to find words
   if choice == "a":
      findOneVowel(dataFile)  
   
   elif choice == "b":
      findWordsMax(dataFile)

   elif choice == "c":
      findCharacters(dataFile)
     
   elif choice == "d":
      findijtx(dataFile)

   elif choice == "e":
      findPalindrome(dataFile)
   
   elif choice =="q":
      print ("Thank you for playing")
      # Close dictionary file
      dataFile.close()
      
   else:
      print ("Incorrect choice. Please try again")