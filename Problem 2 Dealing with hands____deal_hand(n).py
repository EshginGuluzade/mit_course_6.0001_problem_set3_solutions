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