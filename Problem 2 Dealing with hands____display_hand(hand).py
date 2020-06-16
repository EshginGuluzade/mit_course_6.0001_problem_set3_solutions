'''
# mit_course_number_6.0001_problem_set3_solutions
MIT Course: Introduction to Computer Science and Programming in Python

Author: Eshgin Guluzade

Specialty: Mechanical Engineer

Country: Azerbaijan
'''

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

def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
