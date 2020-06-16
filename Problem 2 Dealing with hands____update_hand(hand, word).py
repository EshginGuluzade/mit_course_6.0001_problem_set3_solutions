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