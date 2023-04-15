def print_rangoli(n):
    
    ifen_size = n*2-2
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alp = a[:n]
    alp = alp[::-1]
    st = '-'.join(alp)+'0'

    l = []
    for i in range(ifen_size,0,-2):
        temp = '-'*i+st[:ifen_size-i]
        l.append(temp+alp[n-1-int(i/2)]+temp[::-1])
        
    st = st[:-1] +st[-3::-1]

    l +=[st]+l[::-1]
    for i in l:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)