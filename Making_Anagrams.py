def makeAnagram(a, b):
    # Write your code here

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    number_eliminate = 0
    
    for i in letters:
        n_a = a.count(i)
        n_b = b.count(i)
        
        number_eliminate = number_eliminate + max( n_a - n_b, n_b - n_a )

    return number_eliminate
