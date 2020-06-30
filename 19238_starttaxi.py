from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs_guest(r,c,fuel):
    if (r,c) in guest.keys():
        return r,c,0
    row = col = length = float('inf')
    queue = deque()
    queue.append([r,c,0,fuel])
    visit[r][c] = 1
    while queue:
        pr,pc,cnt,f = queue.popleft()
        if cnt + 1 > length:
            return row, col, length
        if f<0:
            return float('inf'), float('inf'), float('inf')
        for i in range(4):
            nr = pr+dr[i]
            nc = pc+dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc] and not base[nr][nc]:
                visit[nr][nc] = 1
                if (nr,nc) in guest.keys() and length>=cnt+1 and not complete[(nr,nc)]:
                    length = cnt + 1
                    if nr < row:
                        row = nr
                        col = nc
                    elif nr == row:
                        if nc < col:
                            col = nc
                queue.append([nr,nc,cnt+1,f-1])
    return float('inf'), float('inf'), float('inf')

def bfs_dest(r,c,tr,tc,fuel):
    if r==tr and c == tc:
        return 0
    queue = deque()
    queue.append([r,c,0,fuel])
    visit[r][c] = 1
    while queue:
        pr,pc,cnt,f = queue.popleft()
        if f<0:
            return float('inf')
        for i in range(4):
            nr = pr+dr[i]
            nc = pc+dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc] and not base[nr][nc]:
                visit[nr][nc] = 1
                if nr==tr and nc==tc and f-1>=0:
                    return cnt+1
                queue.append([nr,nc,cnt+1,f-1])
    return float('inf')
    


N, M, g = map(int,input().split())
base = [list(map(int,input().split())) for _ in range(N)]
row, col = map(int,input().split())
row -= 1
col -= 1
guest = {}
complete = {}

for _ in range(M):
    sr, sc, er, ec = map(int,input().split())
    guest[(sr-1,sc-1)] = [er-1,ec-1]
    complete[(sr-1,sc-1)] = False

while True:
    visit=[[0]*N for _ in range(N)]
    tr, tc, length = bfs_guest(row,col,g)
    complete[(tr,tc)] = True
    g -= length
    if g <= 0:
        break
    visit=[[0]*N for _ in range(N)]
    length = bfs_dest(tr,tc,guest[(tr,tc)][0],guest[(tr,tc)][1],g)
    if length == float('inf'):
        break
    g += length
    row, col = guest[(tr,tc)][0],guest[(tr,tc)][1]
    if False not in complete.values():
        break

if False in complete.values():
    print(-1)
else:
    print(g)