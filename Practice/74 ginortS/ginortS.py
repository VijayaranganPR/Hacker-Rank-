s = input()
d = {'l':[], 'u':[], 'o':[], 'e':[]}
for i in s:
    if i.islower():
        d['l'] += i
        continue
    if i.isupper():
        d['u'] += i
        continue
    if int(i)%2 == 1:
        d['o'] += i
        continue
    if int(i)%2 == 0:
        d['e'] += i
print(''.join(sorted(d['l'])+sorted(d['u'])+sorted(d['o'])+sorted(d['e'])))