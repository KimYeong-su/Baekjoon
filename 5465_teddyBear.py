import sys
import heapq
input = sys.stdin.readline

N, S = map(int, input().split())
base = [list(input()) for _ in range(N)]
bear_visit = [[False for _ in range(N)]for _ in range(N)]
bee_visit = [[False for _ in range(N)]for _ in range(N)]
bee_now = []
now = []
for i in range(N):
    for j in range(N):
        if base[i][j] == 'G':
            continue
        elif base[i][j] == 'T':
            bear_visit[i][j] = True
            bee_visit[i][j] = True
        elif base[i][j] == 'M':
            bear_visit[i][j] = True
            heapq.heappush(now,(-1,i,j))
        elif base[i][j] == 'D':
            goal = (i,j)
        else:
            bee_now += [(0,i,j)]
            bear_visit[i][j] = True
            bee_visit[i][j] = True

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bee(queue,visit,goal):
    while queue:
        cnt, x, y = heapq.heappop(queue)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if (nx, ny) == goal:
                    return cnt
                visit[nx][ny] = True
                heapq.heappush(queue, (cnt+1, nx, ny))


def bear(queue,visit,gaol,bee_cnt):
    result = []
    for _ in range(S):
        tmp = []
        while queue:
            cnt, x, y = heapq.heappop(queue)
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                    if (nx,ny) == goal:
                        result += tmp
                        return result
                    visit[nx][ny] = True
                    heapq.heappush(tmp, (cnt+1, nx, ny))
        queue = tmp
        result += tmp
    return result


bee_cnt = bee(bee_now,bee_visit,goal)
print(bear(now,bear_visit,goal, bee_cnt))