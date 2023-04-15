from collections import Counter
total_size = int(input())
size_dict = Counter(map(int,input().split()))
number_of_costomers = int(input())


money_earned = 0

for _ in range(number_of_costomers):
    shoe_size, price = map(int,input().split())
    if size_dict[shoe_size]:
        money_earned += price
        size_dict[shoe_size] -=1
print(money_earned)    
