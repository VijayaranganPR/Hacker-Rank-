import math
for _ in range(int(input())):
    n = int(input())
    m = -1
    if n%2 !=0:
        print(-1)
    else:
        temp = int(math.sqrt(n))
        for a in range(temp,n//3+1):
            b = (n**2 - 2*a*n)/(2*n - 2*a)
            c = n-a-b
            product =  a*b*c
            if b == int(b) and product > m:
                m = product
        else:
            print(int(m))
