import sys
input = sys.stdin.readline

R, C, T = map(int, input().rstrip('\n').split())
base = [list(map(int, input().rstrip('\n').split())) for _ in range(R)]

points = []
cleaner = []
for i in range(R):
    for j in range(C):
        if base[i][j] > 0:
            points.append((i,j))
        elif base[i][j] < 0:
            cleaner.append(i)

dr = [0,-1,0,1]
dc = [1,0,-1,0]
r_dr = [0,1,0,-1]
r_dc = [1,0,-1,0]

for _ in range(T):
    tmp  = [[0]*C for _ in range(R)]
    for r,c in points:
        if base[r][c] >= 5:
            spread = (base[r][c])//5
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nc < 0 or nr >= R or nc >= C or base[nr][nc]==-1: continue
                tmp[nr][nc] += spread
                base[r][c] -= spread
        tmp[r][c] += base[r][c]
        base[r][c] = 0
    points = []
    start = (cleaner[0],1)
    idx = 0
    while start != (cleaner[0]-1,0):
        nr, nc = start[0] + dr[idx], start[1] + dc[idx]
        if 0<=nr<cleaner[1] and 0<=nc<C:
            base[nr][nc] = tmp[start[0]][start[1]]
            if tmp[start[0]][start[1]] > 0:
                points.append((nr,nc))
            start = (nr,nc)
        else:
            idx += 1
    for i in range(1,cleaner[0]):
        for j in range(1,C-1):
            if tmp[i][j] > 0:
                points.append((i,j))
            base[i][j] = tmp[i][j]

    start = (cleaner[1],1)
    idx = 0
    while start != (cleaner[1]+1,0):
        nr, nc = start[0] + r_dr[idx], start[1] + r_dc[idx]
        if cleaner[1]<=nr<R and 0<=nc<C:
            base[nr][nc] = tmp[start[0]][start[1]]
            if tmp[start[0]][start[1]] > 0:
                points.append((nr,nc))
            start = (nr,nc)
        else:
            idx += 1
    for i in range(cleaner[1]+1,R-1):
        for j in range(1, C-1):
            if tmp[i][j] > 0:
                points.append((i,j))
            base[i][j] = tmp[i][j]

    base[cleaner[0]][0] = -1
    base[cleaner[1]][0] = -1

answer = 0
for i in range(R):
    for j in range(C):
        if base[i][j] > 0:
            answer += base[i][j]
print(answer)