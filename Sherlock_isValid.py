def isValid(s):
    # Write your code here

    no_repe = list(set(s))
    
    number_cases = [0]*len(no_repe)
        
    for i in range(0, len(no_repe)):
        number_cases[i] = s.count(no_repe[i])
        
    no_repe_cases = list(set(number_cases))
    
    if(len(no_repe_cases) == 1):
        return "YES"
    elif(len(no_repe_cases) > 2):
        return "NO"
    else:
        n_1 = number_cases.count(no_repe_cases[0])
        n_2 = number_cases.count(no_repe_cases[1])
        if(n_1 ==1 and no_repe_cases[0] == 1):
            return "YES"
        elif(n_2 ==1 and no_repe_cases[1] == 1):
            return "YES"
        elif( abs(no_repe_cases[0]-no_repe_cases[1]) == 1 ):
            if(n_1 == 1 or n_2 ==1 ):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

