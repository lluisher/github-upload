def substrCount(n, s):
    counter = 0
    
    i = 0
    while( i <len(s) ):
        letter = s[i]
        number_letter = 1
        for j in range(i+1, len(s)):
            if(s[j] == letter):
                number_letter = number_letter + 1
            else:
                break
        
        #count condition 1
        counter = counter + int(number_letter*(number_letter+1)*0.5)

        #count condition 2
        number_cond_2 = 0
        for j in range(i+number_letter+1, len(s)):
            if(s[j] == letter):
                number_cond_2 = number_cond_2 + 1
            else:
                break
        counter = counter + min(number_cond_2, number_letter)
        
        #jump to the next different letter
        i = i + number_letter
        
    return counter
