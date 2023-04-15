def count_substring(string, sub_string):
    flag = True
    counter = 0
    # while loop will run until no match is found (found == -1)
    while(flag):
        found = string.find(sub_string)
        if(found != -1):
            counter += 1
            # removing the first character of the matched sub string
            string = string[:found] + string[found+1:]
        else:
            flag = False
            
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)