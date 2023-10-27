int(input())
arr = list(map(int, input().split()))

print(any(map(lambda x: str(x)==str(x)[::-1], (arr))) if all(map(lambda x: x>-1, (arr))) else False)