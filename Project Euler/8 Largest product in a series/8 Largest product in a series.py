t = int(input())
for i in range(t):
    n,k = [i for i in input().split()]
    n,k = [int(n),int(k)]
    num = input()
    

    maxtop = 0


    # making range from 0 to n-k+1     
    for j in range(n-k+1):

        # Spliting the num
        temp = num[j:j+k]
        maxin = 1
        for x in temp: 
            maxin *= int(x)
        
        if maxtop <maxin:
            maxtop = maxin
        
    print(maxtop)