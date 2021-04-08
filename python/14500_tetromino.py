import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

visit = [[False]*M for _ in range(N)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(r, c, cnt, tmp):
    global answer
    if not cnt%4:
        if tmp > answer:
            answer = tmp
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<M and not visit[nr][nc]:
            visit[nr][nc] = True
            dfs(nr,nc,cnt+1, tmp+base[nr][nc])
            visit[nr][nc] = False
    if cnt%4==1:
        if 0<=r<N-1 and 2<=c+2<M:
            answer = max(answer, tmp+base[r][c+1]+base[r][c+2]+base[r+1][c+1])
        if 0<r<N and 2<=c+2<M:
            answer = max(answer, tmp+base[r][c+1]+base[r][c+2]+base[r-1][c+1])
        if 2<=r+2<N and 0<=c<M-1:
            answer = max(answer, tmp+base[r+1][c]+base[r+2][c]+base[r+1][c+1])
        if 2<=r+2<N and 0<c<M:
            answer = max(answer, tmp+base[r+1][c]+base[r+2][c]+base[r+1][c-1])


answer = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(i,j,1,base[i][j])
        visit[i][j] = False

print(answer)