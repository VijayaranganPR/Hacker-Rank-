palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist and len(str(a))>5:
            palindromelist.append(a)
palindromelist.sort()

n = int(input())
for _ in range(n):
    a = int(input())
    for i in palindromelist:
        if i >= a:
            ind = palindromelist.index(i)
            print(palindromelist[ind-1])
            break