def swap_case(s):
    new_s = ''
    for char in s:
        new_s += char.upper() if(char.islower()) else char.lower()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)