def count_substring(string,sub):
    count = 0
    for x,y in enumerate(string):
        if sub[0] == y:
            for j,k in enumerate(sub):
                try:
                    if k != string[x+j]:
                        break
                except:
                    break
            else:
                count += 1
    
    return count
            

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)