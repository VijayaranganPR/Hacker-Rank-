import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*itertools.product(A, B))