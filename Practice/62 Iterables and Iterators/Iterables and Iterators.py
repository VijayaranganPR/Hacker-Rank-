from itertools import combinations
n = int(input())
letters = list(map(str, input().split()))
k = int(input())
combine = list(combinations(range(n), k))
index = [i for i,j in enumerate(letters) if j == 'a']
count = 0
for i in combine:
    for j in i:
        if j in index:
            count +=1
            break
print(count/len(combine))