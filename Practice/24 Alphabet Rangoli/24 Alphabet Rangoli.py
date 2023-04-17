def print_rangoli(size):
    if (size == 1):
        print('a')
        return
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = alphabet[size-1::-1]
    space = size*4 - 3
    pattern = ['-'.join(alphabet[:i+1] + alphabet[::-1][size-i:]).center(space, '-') for i in range(size)]
    print('\n'.join(pattern + pattern[size-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)