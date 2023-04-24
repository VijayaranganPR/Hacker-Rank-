from collections import namedtuple
n = int(input())
student = namedtuple('student', input().split())
print(sum([int(student(*input().split()).MARKS) for i in range(n)])/n)