import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
base = [tuple(map(int,input().rstrip('\n').split())) for _ in range(N)]

answer = 0
def dfs(day, result):
    global answer
    if answer < result:
        answer = result
    for i in range(day,N):
        if base[i][0] + i <= N:
            dfs(i+base[i][0], result+base[i][1])

dfs(0,0)
print(answer)