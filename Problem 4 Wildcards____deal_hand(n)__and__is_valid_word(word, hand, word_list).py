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
