n = int(input())
l = [int(input()) for i in range(n)]
result = []
for element in l:
    mini = 1
    while (True):
        for i in range(2,element+1):
            if mini%i !=0:
                mini+=1
                break
            else:
                continue
        else:
            result.append(mini)
            break
        
for i in result:
    print(i)
