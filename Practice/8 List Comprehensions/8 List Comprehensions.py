if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    [ [ [ result.append([i,j,k]) for k in range(z+1)] for j in range(y+1)] for i in range(x+1)]
    print([i for i in result if sum(i) != n])