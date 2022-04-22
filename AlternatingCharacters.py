def alternatingCharacters(s):
    # Write your code here
    number_elimination = 0
    for i in range(0, len(s)-1):
        if(s[i] == s[i+1] ):
            number_elimination = number_elimination + 1
    
    return number_elimination
