from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs_guest(r,c,fuel):
    if base[r][c]>1:
        return r, c, 0
    queue = deque()
    queue.append([r,c,0,fuel])
    visit[r][c] = 1
    row = col = length = float('inf')
    while queue:
        pr, pc, cnt, f = queue.popleft()
        if length < cnt: continue
        if base[pr][pc] > 1:
            length = cnt
            if row > pr:
                row = pr
                col = pc
            elif row == pr and col > pc:
                col = pc
        if f<=0:continue
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc]:
                if base[nr][nc]!=1:
                    visit[nr][nc]=1
                    queue.append([nr,nc,cnt+1,f-1])

    if row != float('inf'):
        base[row][col] = 0
    return row, col, length

def bfs_dest(r,c,tr,tc,fuel):
    queue = deque()
    queue.append([r,c,0,fuel])
    visit[r][c]=1
    while queue:
        pr,pc,cnt,f = queue.popleft()
        if f<0:
            return float('inf'), float('inf'), float('inf')
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc] and base[nr][nc]!=1:
                if nr == tr and nc == tc and f-1>=0:
                    return nr, nc, cnt + 1
                else:
                    queue.append([nr,nc,cnt+1,f-1])
    return float('inf'), float('inf'), float('inf')

N, M, g = map(int,input().split())

base = [list(map(int,input().split())) for _ in range(N)]
sr, sc = map(int,input().split())
sr -= 1
sc -= 1
dest = {}
for i in range(2,M+2):
    gr, gc, tr, tc = map(int,input().split())
    base[gr-1][gc-1] = i
    dest[(gr-1, gc-1)] = [tr-1, tc-1]

for num in range(M):
    visit = [[0]*N for _ in range(N)]
    gr, gc, length = bfs_guest(sr,sc,g)
    g -= length
    if g<=0:
        g = -1
        break
    visit = [[0]*N for _ in range(N)]
    sr, sc, length = bfs_dest(gr, gc, dest[(gr,gc)][0], dest[(gr,gc)][1], g)
    if length == float('inf'):
        g = -1
        break
    g += length

print(g)