import re
s = re.search(r"([a-zA-Z0-9])(\1)", input())
print(s.group(0)[0] if s else -1)