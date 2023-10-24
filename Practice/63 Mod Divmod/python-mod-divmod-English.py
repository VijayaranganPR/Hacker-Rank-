a = int(input())
b = int(input())

# divmod(a, b) -> (a//b, a%b)
r = divmod(a, b)

# printing in requested format
print(r[0])
print(r[1])
print(r)