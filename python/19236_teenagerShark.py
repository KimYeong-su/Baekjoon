import sys
from copy import deepcopy
input = sys.stdin.readline

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]
# 물고기 이동 가능(45도 씩 방향 수정) - 빈칸, 다른 물고기가 있는 칸, 상어가 없는 칸
# 물고기 이동 불가능(하면 물고기 이동 x) - 상어가 있는 칸, 경계를 넘는 칸
# 상어가 이동가능 - 물고기가 있는 칸
maps = []
fish_maps = {}
for i in range(4):
    tmp = list(map(int, input().rstrip('\n').split()))
    tmp1 = []
    for j in range(0,8,2):
        tmp1.append([tmp[j], tmp[j+1]-1])
        fish_maps[tmp[j]] = [i,j//2]
    maps.append(tmp1)

answer = 0
def dfs(x,y,d,total,b,f):
    global answer
    base = deepcopy(b)
    fish_maps = deepcopy(f)
    
    result = base[x][y][0]
    dirs = base[x][y][1]
    fish_maps[base[x][y][0]] = []
    base[x][y] = []
    
    answer = max(answer, total+result)
    # 물고기 이동
    for num in range(1,17):
        if not fish_maps[num]: continue
        r,c = fish_maps[num]
        d = base[r][c][1]
        n = 0
        while n < 8:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<4 and 0<=nc<4 and (nr,nc) != (x,y):
                if base[nr][nc]:
                    fish_maps[num], fish_maps[base[nr][nc][0]] = fish_maps[base[nr][nc][0]], fish_maps[num]
                else:
                    fish_maps[num] = [nr,nc]
                base[r][c][1] = d
                base[nr][nc], base[r][c] = base[r][c], base[nr][nc]
                break
            d += 1
            n += 1
            if d > 7:
                d %= 8

    for i in range(1,4):
        nx = x + dr[dirs]*i
        ny = y + dc[dirs]*i
        if 0<=nx<4 and 0<=ny<4 and base[nx][ny]:
            dfs(nx, ny, dirs, result + total, base, fish_maps)
    
dfs(0,0,0,0,maps,fish_maps)
print(answer)