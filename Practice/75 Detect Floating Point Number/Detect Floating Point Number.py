for i in range(int(input())):
    a = input()
    try:
        float(a)
    except:
        print(False)
    else:
        print(True if '.' in str(a) else False)