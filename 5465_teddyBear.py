import sys
import heapq
input = sys.stdin.readline

N, S = map(int, input().split())
base = [list(input()) for _ in range(N)]
bee_visit = [[0 for _ in range(N)]for _ in range(N)]
bee_now = [] # bee_queue
now = [] # bear_queue
for i in range(N):
    for j in range(N):
        if base[i][j] == 'G':
            bee_visit[i][j] = -2
        elif base[i][j] == 'T':
            bee_visit[i][j] = -1
        elif base[i][j] == 'M':
            heapq.heappush(now,(-1,i,j))
        elif base[i][j] == 'D':
            goal = (i,j)
        else:
            bee_now += [(0,i,j)]
            bee_visit[i][j] = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bee_bfs(queue, visit):
    tmp = 0
    while queue:
        cnt,x,y = heapq.heappop(queue)
        if tmp < cnt:
            tmp = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == -2:
                visit[nx][ny] = cnt+1
                heapq.heappush(queue,(cnt+1, nx, ny))
    return tmp
        
left = 0
right = bee_bfs(bee_now, bee_visit)

def bear_bfs(queue, wait):
    visit = [[False for _ in range(N)]for _ in range(N)]
    while queue:
        cnt, x, y = heapq.heappop(queue)
        if visit[x][y]: continue
        visit[x][y] = True
        if base[x][y]=='D':
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if base[nx][ny]=='G':
                    if ((cnt+1)//S+1+wait)<bee_visit[nx][ny]+1:
                        heapq.heappush(queue,(cnt+1,nx,ny))
                if base[nx][ny]=='D':
                    heapq.heappush(queue,(cnt+1, nx, ny))
    return False

def initialize(queue):
    tmp = []
    for i in queue:
        heapq.heappush(tmp,i)
    return tmp
                
answer = -1
while left <= right:
    mid = (left + right) // 2

    queue = initialize(now)

    if bear_bfs(queue,mid):
        if answer < mid:
            answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
