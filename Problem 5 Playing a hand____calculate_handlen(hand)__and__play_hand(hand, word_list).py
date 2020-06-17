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


def calculate_handlen(hand):
    total = 0
    for value in hand.values():
        total += value
    return total


def play_hand(hand, word_list):


    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    word_score = 0
    total_score = 0
        # Display the hand
    while (calculate_handlen(hand) > 0 ):
        print('Current Hand: ', end=' '); 
        print(display_hand(hand))
        
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
                # and the updated total score

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
                
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