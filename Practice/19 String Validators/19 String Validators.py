if __name__ == '__main__':
    s = input()
    for _ in s:
        if _.isalnum():
            print(True)
            break
    else:
        print(False)
    for _ in s:
        if _.isalpha():
            print(True)
            break
    else:
        print(False)
    for _ in s:
        if _.isdigit():
            print(True)
            break
    else:
        print(False)
    for _ in s:
        if _.islower():
            print(True)
            break
    else:
        print(False)
    for _ in s:
        if _.isupper():
            print(True)
            break
    else:
        print(False)