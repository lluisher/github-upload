
def commonChild(s1, s2):
    # Write your code here
   
    
    n1 = len(s1)
    n2 = len(s2)
    
    #counts = [[0]*(n2+1) for i in range(n1+1)]
    
    count = [0]*(n2+1)
    #count_new = [0]*(n2+1)
    
      
    for i in range(0, n1):
        left = 0
        #count_new = [0]*(n2+1)
        for j in range(0, n2):
            temp = count[j+1]
            
            if( s1[i] == s2[j] ):
                count[j+1] = left + 1 
            else:
                count[j+1] = max( count[j], count[j+1] )

            left = temp

    
    return count[-1]

