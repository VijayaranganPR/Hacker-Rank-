from itertools import permutations
string, size = input().split()
size = int(size)
result_list = ["".join(i) for i in list(permutations(string,size))]
result_list.sort()
print(*result_list, sep = "\n")
