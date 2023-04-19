def merge_the_tools(string, k):
    final = []
    for i in range(k, len(string) + k, k):
        min_string = ''
        for j in string[i-k: i]:
            if(j not in min_string):
                min_string += j
        final.append(min_string)
    print('\n'.join(final))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)