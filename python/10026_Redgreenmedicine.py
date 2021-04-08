dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs1(row,col,color):
    stack = [(row,col)]
    while stack:
        x,y = stack.pop()
        if not visit1[x][y]: visit1[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visit1[nx][ny] and base[nx][ny]==color:
                stack.append((nx,ny))

def dfs2(row,col,color):
    stack = [(row,col)]
    while stack:
        x,y = stack.pop()
        if not visit2[x][y]: visit2[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visit2[nx][ny]:
                if color in ['R','G']:
                    if base[nx][ny] in ['R','G']:
                        stack.append((nx,ny))
                else:
                    if base[nx][ny] == color:
                        stack.append((nx,ny))



N = int(input())
base = []
visit1 = [[0]*N for _ in range(N)]
visit2 = [[0]*N for _ in range(N)]

for _ in range(N):
    base.append(list(input()))

result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if not visit1[i][j]:
            dfs1(i,j,base[i][j])
            result1 += 1
        if not visit2[i][j]:
            dfs2(i,j,base[i][j])
            result2 += 1
print(result1, result2)
