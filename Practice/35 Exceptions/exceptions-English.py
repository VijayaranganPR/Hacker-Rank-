for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print(f'Error Code: {e}')