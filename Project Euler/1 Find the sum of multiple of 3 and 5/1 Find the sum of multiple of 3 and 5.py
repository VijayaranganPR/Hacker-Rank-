# to find the nth element of the arithmetic series
# x = a + (n-1)*d
# to find the last multiple number of a range 
# x = x - x%3
# to find teh sum of the arithmetic series
# x = n(n+1)//2
# we can also use x = n/2*(2*a +(n-1)*d)
# Now the variables are n, a, and d
# n is the nth element
# a is the first element
# d is the commen difference


def ap(x):
    result = x*(x+1)//2
    return result

n=int(input())
while n!=0:
    nu=int(input())
    nu-=1
    a=nu//3
    b=nu//5
    c=nu//15
    print(3*ap(a)+5*ap(b)-15*ap(c))
    n-=1