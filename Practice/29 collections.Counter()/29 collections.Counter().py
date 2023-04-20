import collections
x = int(input())
all_shoes = collections.Counter(map(int, input().split()))
total_earning = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if all_shoes[size]:
        all_shoes[size] -= 1
        total_earning += price
print(total_earning)