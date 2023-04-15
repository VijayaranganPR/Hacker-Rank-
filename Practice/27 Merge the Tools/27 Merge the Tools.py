def merge_the_tools(string, k):
    l = [string[i:i+k] for i in range(0,len(string),k)]
    result = []
    for i in l:
        temp = ""
        for j in i:
            if j in temp:
                continue
            else:
                temp+=j
        result.append(temp)
    print(*result,sep = "\n")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)