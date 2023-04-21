from collections import defaultdict

n,m = map(int, input().split())
index = defaultdict(list)
for i in range(n):
    index[input()].append(i+1)

m_list = [input() for i in range(m)]

for i in m_list:
    print(*index[i] if (index[i]) else [-1])