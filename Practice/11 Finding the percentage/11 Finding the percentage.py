n = int(input())
dic = {}
for i in range(n):
    names, *lines = input().split()
    scores = list(map(float,lines))
    dic[names] = scores
query_name = input()
ans = dic[query_name]
print(f"{sum(ans)/len(ans):.2f}")
