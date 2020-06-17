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