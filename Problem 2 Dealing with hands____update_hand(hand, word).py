'''
# mit_course_number_6.0001_problem_set3_solutions

MIT Course 6.0001: Introduction to Computer Science and Programming in Python

Author: Eshgin Guluzade

Specialty: Mechanical Engineer

Country: Azerbaijan

My LinkedIn: https://www.linkedin.com/in/eshginguluzade/

My Quora: https://www.quora.com/profile/Eshgin-Guluzade

My Youtube Channel: https://www.youtube.com/channel/UCr6yufueEVaXBHgM8x1YlTw
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
