import re
s = input()
k = input()
found_match = False
len_s = len(s)
len_k = len(k)-1
for i in range(len_s+1):
    substring_s = s[0+i:]
    m = re.match(k,substring_s)
    if m != None:
        result = (i,i+len_k)
        print(result)
        found_match = True
    else:
        pass
if found_match == False:
    print("(-1, -1)")
