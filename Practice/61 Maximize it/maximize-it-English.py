from itertools import product
# spliting the k and m
k, m = map(int,input().split())

# for k list, getting the input and indexing from [1:] and using itertools.product to find the permutation 
contents = list(product(*[list(map(int,input().split()))[1:] for i in range(k)]))

# storing content by finding the square, then adding and using module with m 
result = [(sum(map(lambda x: x**2, i)))%m for i in contents]

# printing the result
print(max(result))
