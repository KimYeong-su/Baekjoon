import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip('\n'))
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]

fish_count = [0 for _ in range(7)]
queue = []
for i in range(N):
    for j in range(N):
        if 0<base[i][j]<9:
            fish_count[base[i][j]]+=1
        elif base[i][j] == 9:
            visit[i][j] = True
            heapq.heappush(queue,(0,i,j))
            base[i][j] = 0

dr = [-1,0,0,1]
dc = [0,-1,1,0]
answer = 0
shark_size = 2
prey = 0
while queue:
    for i in range(1,7):
        if i<shark_size and fish_count[i]>0: break
    else:
        break
    cnt,r,c = heapq.heappop(queue)
    if 0<base[r][c]<shark_size:
        visit = [[False]*N for _ in range(N)]
        visit[r][c] = True
        fish_count[base[r][c]]-=1
        base[r][c] = 0
        answer += cnt
        queue = [(0,r,c)]
        prey += 1
        if prey == shark_size:
            shark_size += 1
            prey = 0
        continue
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<N and not visit[nr][nc]:
            if 0<=base[nr][nc]<=shark_size:
                visit[nr][nc] = True
                heapq.heappush(queue,(cnt+1,nr,nc))
print(answer)