from itertools import permutations
text, k = input().split()
print(*[''.join(i) for i in sorted(permutations(text,int(k)))], sep = '\n')