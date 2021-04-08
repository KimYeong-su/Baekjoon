import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
base = [list(map(int, input().split()))for _ in range(N)]
visit = [[False]*N for _ in range(N)]
case = []
for i in range(N):
    for j in range(N):
        if base[i][j] == 1:
            visit[i][j] = True
        elif base[i][j] == 2:
            case.append((i,j))

start = []
def combinations(n, now, tmp):
    global start
    if len(tmp) == M:
        start.append(tmp)
        return
    visit = [False] * n
    for i in range(now,n):
        if visit[i]: continue
        visit[i] = True
        combinations(n, i+1, tmp+[i])
        visit[i] = False

combinations(len(case), 0, [])
answer = float('inf')

for c in start:
    tmp_visit = [[False]*N for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                tmp_visit[i][j] = True

    for i in c:
        row,col = case[i]
        tmp_visit[row][col] = True
        heapq.heappush(queue, (0,row,col))
    
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    tmp = 0
    while queue:
        cnt, row, col = heapq.heappop(queue)
        if cnt > tmp and base[row][col] == 0:
            tmp = cnt
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<N and 0<=nc<N and not tmp_visit[nr][nc]:
                tmp_visit[nr][nc] = True
                heapq.heappush(queue, (cnt+1,nr,nc))
    for r in tmp_visit:
        if False in r:
            break
    else:
        if answer > tmp:
            answer = tmp
            

if answer == float('inf'):
    print(-1)
else:
    print(answer)