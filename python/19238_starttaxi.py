import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().rstrip('\n').split())
guest = [list(map(int, input().rstrip('\n').split()))for _ in range(N)]
destination = {}


start = list(map(lambda x: int(x)-1, input().rstrip('\n').split()))
start += [fuel]
for idx in range(2,2+M):
    x1,y1,x2,y2 = map(lambda x : int(x)-1, input().rstrip('\n').split())
    guest[x1][y1] = idx
    if (x2,y2) in destination:
        destination[(x2,y2)] += [idx]
    else:
        destination[(x2,y2)] = [idx]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(M):
    g_visit = [[0]*N for _ in range(N)]
    d_visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if guest[i][j]==1:
                g_visit[i][j] = 1
                d_visit[i][j] = 1

    queue = [tuple(start)]
    g_visit[start[0]][start[1]] = 1
    remain = 0
    sx, sy = float('inf'), float('inf')
    guest_num = float('inf')
    while queue:
        x,y,f = queue.pop(0)
        if guest[x][y] > 1 and remain <= f:
            if sx > x:
                sx = x
                sy = y
                remain = f
                guest_num = guest[x][y]
                continue
            elif sx == x:
                if sy > y:
                    sy =y
                    remain = f
                    guest_num = guest[x][y]
                    continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not g_visit[nx][ny] and f>0:
                queue.append((nx,ny,f-1))
                g_visit[nx][ny] = 1
    if guest_num == float('inf'):
        break
    guest[sx][sy] = 0
    queue = [(sx,sy,remain,0)]
    d_visit[sx][sy] = 1
    while True:
        x, y, r, cnt = queue.pop(0)
        if (x,y) in destination and guest_num in destination[(x,y)]:
            start = [x,y,r+cnt]
            destination[(x,y)].remove(guest_num)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not d_visit[nx][ny] and r-cnt > 0:
                queue.append((nx,ny,r,cnt+1))
                d_visit[nx][ny] = 1
        if not queue:
            print(-1)
            exit()
else:
    print(start[2])
    exit()
print(-1)
