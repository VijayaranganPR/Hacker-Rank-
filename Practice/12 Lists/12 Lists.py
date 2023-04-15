if __name__ == '__main__':
    l = []
    N = int(input())
    for _ in range(N):
        input_test = input().split()
        if(input_test[0] == 'insert'):
            l.insert(int(input_test[1]), int(input_test[2]))
        elif(input_test[0] == 'print'):
            print(l)
        elif(input_test[0] == 'remove'):
            l.remove(int(input_test[1]))
        elif(input_test[0] == 'append'):
            l.append(int(input_test[1]))
        elif(input_test[0] == 'sort'):
            l.sort()
        elif(input_test[0] == 'pop'):
            l.pop()
        elif(input_test[0] == 'reverse'):
            l.reverse()