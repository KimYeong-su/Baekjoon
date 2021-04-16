import sys
input = sys.stdin.readline

N, M, H = map(int, input().rstrip('\n').split())
if M == 0:
    print(0)
    exit()

maps = [[False]*N for _ in range(H)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().rstrip('\n').split())
    maps[a][b] = True

answer = 4
def check():
    for s in range(N):
        tmp = s
        for x in range(H):
            if maps[x][tmp]:
                tmp += 1
            elif tmp > 0 and maps[x][tmp-1]:
                tmp -= 1
        if s != tmp:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if cnt >= answer:
        return
    if check():
        if answer > cnt:
            answer = cnt
        return
    for i in range(x,H):
        k = y if i==x else 0
        for j in range(k,N-1):
            if not maps[i][j] and not maps[i][j+1]:
                maps[i][j] = True
                dfs(cnt+1, i, j+2)
                maps[i][j] = False

dfs(0,0,0)
print(answer) if answer < 4 else print(-1)