dx = [1,-1,1,-1]
dy = [1,-1,-1,1]

def check(n,row):
    global result
    if row == N:
        result += 1
        return
    for i in range(n):
        if visit[i]: continue
        flag = True
        for j in range(4):
            x = row
            y = i
            while True:
                nx = x + dx[j]
                ny = y + dy[j]
                if 0<=nx<N and 0<=ny<N:
                    if base[nx][ny]:
                        flag = False
                        break
                    x = nx
                    y = ny
                else:
                    break
        if flag:
            visit[i] = True
            base[row][i] = 1
            check(n,row+1)
            base[row][i] = 0
            visit[i] = False

N = int(input())
base=[[0]*N for _ in range(N)]
result = 0
visit = [False]*N
check(N,0)
print(result)