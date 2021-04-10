import sys
from copy import deepcopy
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
queue = []
for i in range(N):
    for j in range(M):
        if 0<base[i][j]<6:
            queue.append((base[i][j],i,j))

directions = [(0,1),(1,0),(0,-1),(-1,0)] #우, 상, 좌, 하


answer = float('inf')

def check(base, dirs, x, y):
    tmp = deepcopy(base)
    for d in dirs:
        while True:
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            if 0<=nx<N and 0<=ny<M:
                if tmp[nx][ny] == 6:break
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
                x = nx
                y = ny
            else:
                break
    return tmp


def dfs(base,queue,idx):
    global answer
    if idx == len(queue):
        tmp = 0
        for i in range(N):
            tmp += base[i].count(0)
        if tmp < answer:
            answer = tmp
        return

    kind, x, y = queue[idx]
    if kind == 1:
        for i in range(4):
            next_maps = check(base, [i], x, y)
            dfs(next_maps, queue, idx+1)
    elif kind == 2:
        for i in [[0,2],[1,3]]:
            next_maps = check(base, i, x, y)
            dfs(next_maps, queue, idx+1)
    elif kind == 3:
        for i in [[0,1],[1,2],[2,3],[3,0]]:
            next_maps = check(base, i, x, y)
            dfs(next_maps, queue, idx+1)
    elif kind == 4:
        for i in [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]:
            next_maps = check(base, i, x, y)
            dfs(next_maps, queue, idx+1)
    elif kind == 5:
        next_maps = check(base, [0,1,2,3], x, y)
        dfs(next_maps, queue, idx+1)

dfs(base,queue, 0)
print(answer)