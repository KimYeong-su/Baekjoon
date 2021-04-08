import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r,c,d = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]

dr = [-1,0,1,0] # 북 동 남 서
dc = [0,1,0,-1]

answer = 0
flag = False
while True:
    # 1번 시행
    if not base[r][c]:
        answer += 1
        base[r][c] = 2

    # 2번 시행
    flag1 = False
    while True:
        for i in range(4):
            if 0<=r+dr[i]<N and 0<=c+dc[i]<M and base[r+dr[i]][c+dc[i]] == 0:
                nr = r + dr[d-1]
                nc = c + dc[d-1]

                if 0<=nr<N and 0<=nc<M and base[nr][nc] == 0: # 2.a
                    r = nr
                    c = nc
                    d = (d-1)%4
                    flag1 = True
                else: # 2.b
                    d = (d-1)%4
                break
        else:
            if 0<=r+dr[(d+2)%4]<N and 0<=c+dc[(d+2)%4]<M and base[r+dr[(d+2)%4]][c+dc[(d+2)%4]] in [0,2]: # 2.c
                r += dr[(d+2)%4]
                c += +dc[(d+2)%4]
            else: # 2.d
                flag = True
                break
        if flag1:
            break
    if flag:
        break
print(answer)
