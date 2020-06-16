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

def deal_hand(n):
    
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
