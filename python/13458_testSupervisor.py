import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
A = list(map(int, input().rstrip('\n').split()))
B, C = map(int, input().rstrip('\n').split())

answer = 0
for a in A:
    answer += 1
    tmp = a-B
    if tmp<1: continue
    answer += tmp//C
    if tmp%C:
        answer += 1
print(answer)