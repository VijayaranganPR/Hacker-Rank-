n = int(input())
for i in range(n):

    x = int(input())
    l = []
    a = 0
    b = 1
    while (True):
        a,b = b,a+b
        if b>x:
            break
        l.append(b)
    ans = []
    for i in l:
        if i%2 ==0:
            ans.append(i)
    print(sum(ans))
