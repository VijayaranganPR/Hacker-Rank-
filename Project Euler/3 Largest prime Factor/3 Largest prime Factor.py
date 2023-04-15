t = int(input())
for i in range(t):
    n = int(input())
    s = set()

    def func(n):
        while n%2 ==0:
            s.add(2)
            n = n//2

        for i in range(3,round(n**0.5)+1,2):
            while n%i == 0:
                s.add(i)
                n = n//i
        if n>2:
            s.add(n)



    func(n)
    print(max(s))