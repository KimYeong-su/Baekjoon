def virus(arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    s = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                s.append((i,j))
                while len(s)!=0:
                    x,y = s.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<M:
                            if arr[nx][ny]==0:
                                arr[nx][ny]=4
                                s.append((nx,ny))


N, M = map(int,input().split())

base = [list(map(int,input().split()))for _ in range(N)]

p = []

# 벽 세울 수 있는 가능성 찾기
for x1 in range(N):
    for y1 in range(M):
        if base[x1][y1]==0:
            for x2 in range(N):
                for y2 in range(M):
                    if (x1,y1)!=(x2,y2):
                        if base[x2][y2]==0:
                            for x3 in range(N):
                                for y3 in range(M):
                                    if (x1,y1)!=(x3,y3) and (x2,y2)!=(x3,y3):
                                        if base[x3][y3]==0:
                                            p.append((x1,y1,x2,y2,x3,y3))
# print(len(p))
max=0
while len(p)!=0:
    x1,y1,x2,y2,x3,y3 = p.pop()
    base[x1][y1], base[x2][y2], base[x3][y3] = 3, 3, 3
    virus(base)
    # for row in base:
    #     print(row)
    cnt=0
    for i in range(N):
        for j in range(M):
            if base[i][j]==0:
                cnt +=1
            if base[i][j]==3 or base[i][j]==4:
                base[i][j]=0
    if max<cnt:
        max = cnt
    # print(cnt)
    # print()

print(max)