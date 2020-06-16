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