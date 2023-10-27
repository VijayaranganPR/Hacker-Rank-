cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    l = []
    if n == 1:
        l = [0]
    elif n == 2:
        l = [0, 1]
    else:
        a = 0 
        b = 1
        for i in range(n):
            l.append(a)
            a,b = b, a+b
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))