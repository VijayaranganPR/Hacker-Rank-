import textwrap

def wrap(string, max_width):
    l = textwrap.wrap(string,max_width)
    for i,j in enumerate(l):
        if i == len(l)-1:
            return j
        else:
            print(j)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)