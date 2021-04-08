import sys
input = sys.stdin.readline

N, L, R = map(int, input().rstrip('\n').split())
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

answer = 0
dr = [0,0,-1,1]
dc = [1,-1,0,0]
while True:
    visit = [[False]*N for _ in range(N)]
    count = [0]*(N*N+1)
    graph = {}
    idx = 1
    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue
            visit[i][j] = True
            graph[idx] = [(i,j)]
            count[idx] += base[i][j]
            queue = [(i,j)]
            while queue:
                r,c = queue.pop(0)
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0<=nr<N and 0<=nc<N and not visit[nr][nc] and L<=abs(base[r][c]-base[nr][nc])<=R:
                        visit[nr][nc] = True
                        graph[idx] += [(nr,nc)]
                        queue.append((nr,nc))
                        count[idx] += base[nr][nc]
            idx += 1
    n = len(graph.keys()) 
    if n == N*N:
        break
    answer += 1
    for i in graph.keys():
        if len(graph[i])<2: continue
        devide = count[i]//len(graph[i])
        for r,c in graph[i]:
            base[r][c] = devide
    
print(answer)