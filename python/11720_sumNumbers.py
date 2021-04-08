import sys
input = sys.stdin.readline

N = int(input())
base = list(input())
answer = 0
for s in base[:-1]:
    answer += int(s)
print(answer)