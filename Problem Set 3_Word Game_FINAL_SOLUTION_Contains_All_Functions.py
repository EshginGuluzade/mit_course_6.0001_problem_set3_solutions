# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
overall_score = 0
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
     points = 0
     second_component = 0
     word = word.lower()
     
     for i in word:
             if i in SCRABBLE_LETTER_VALUES:
                 points = points + SCRABBLE_LETTER_VALUES[i]
             else:
                 continue
     
     second_component = (7*len(word)) - (3 * (n - len(word)))
     
     if second_component < 1:
         second_component = 1
     
     return points * second_component

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    #print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    
    x = random.choice(VOWELS)
    hand[x] = hand.get(x, 0) + 1
    hand['*'] = hand.pop(x) 

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    
    word = word.lower()
    uphand = hand.copy()
    for i in word:
        if i in uphand:
           uphand[i] -=1
           if uphand[i] == 0:
               del(uphand[i])
           else:
               continue
    return  uphand

#
# Problem #3: Test word validity
#

def is_valid_word(word, hand, word_list):
    
     word = word.lower()
     c=0
     s=0
     handnew = hand.copy()
     
     def convert(li): 
  
    # initialization of string to "" 
         new = "" 
  
    # traverse in the string  
         for x in li: 
           new += x  
  
    # return string  
         return new
     
     ####################################################
     
     if '*' in word:
             s = word.find('*')
             for let in VOWELS:
                 l = list(word)
                 l[s] = let
                 l = convert(l)
                 if l in word_list:
                     word = l
                     break
                 else:
                     continue
             if l in word_list:
                 word = l
             else:
                 return False
             handnew[let] = 1
        
     
     ####################################################
        
     if word in word_list :
         for i in word:
             if i in handnew:
                 c+=1
                 handnew[i]-=1
                 if handnew[i] == 0:
                     del(handnew[i])
             else:
                 return False
                 break
         if c == len(word):
             return True
     else:
         return False
                 
     
                 
     
     
                 
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    total = 0
    for value in hand.values():
        total += value
    return total

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    word_score = 0
    total_score = 0
        # Display the hand
    while (calculate_handlen(hand) > 0 ):
        print('Current Hand: ', end=' '); 
        (display_hand(hand))
        
        # Ask user for input
        word = input('Enter word, or "!!" to indicate that you are finished: ')

        # If the input is two exclamation points:
        if word == '!!':
        
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list) == True:
                # Tell the user how many points the word earned,
                word_score = get_word_score(word, len(hand))
                total_score = total_score + word_score
                print(word, 'earned', word_score, 'points. Total: ', total_score)
                print(' ')
                # and the updated total score

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
                print(' ')
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if word == '!!':
        print('Total score: ', total_score)
        
    else:
        print('Ran out of letters. Total score: ', total_score)
    # Return the total score as result of function
    return total_score
    



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    herfler = 'aeioubcdfghjklmnpqrstvwxyz'
    if letter in hand:
        for i in hand.keys():
           herfler = herfler.replace(i, '')
        new_letter = random.choice(herfler)
        hand[new_letter] = hand[letter]
        del(hand[letter])
        new_hand = hand
        return new_hand
    else:
        return hand
           
           
    
def play_game(word_list):


        numberOfSubs = 0
        numberOfReply = 0

        new_score = 0
        old_score = 0
    
    #for hands in range (numberOfHands):
        hand = deal_hand(HAND_SIZE)  
        old_hand = hand.copy()
        (display_hand(hand))
        
        if numberOfSubs == 0:
            subs_yes_no = input('Would you like to substitute a letter? ')
            if subs_yes_no == 'yes':
                letter = input('Which letter would you like to replace: ')
                hand = substitute_hand(hand, letter)
                old_hand = hand.copy()
                numberOfSubs = 1
            else:
                print(' ')
                numberOfSubs = 1
        #else:
        #    continue
        
            
        old_score = play_hand(hand, word_list)
        print('Total score for this hand: ', old_score)
        print('------------------------------------')
        if numberOfReply == 0:
            replay  = input('Would you like to replay the hand? ')
            if replay == 'yes':
                new_score = play_hand(old_hand, word_list)
                print('Total score for this hand: ', new_score)
                print('------------------------------------')
                numberOfReply = 1
            else:
                numberOfReply = 1
                
        #else:
        #    continue
        
        global overall_score        
        overall_score += max(old_score, new_score)
        
        #hands += 1
        
            
        
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    numberOfHands = int(input('Enter total number of hands: '))
    #global overall_score
    for hands in range (numberOfHands):
       play_game(word_list)
       hands+=1
    print('Total score over all hands: ', overall_score)
    
