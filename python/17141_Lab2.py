#재귀함수를 이용한 조합 만들기 https://jebae.github.io/2018/11/13/combination-using-recursion/
def check(arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    stack = []
    stack2 = []

    for a in arr:
        x,y = a
        stack.append((x,y))
        stack2.append(0)

    while len(stack)!=0:
        px,py = stack.pop(0)
        cnt = stack2.pop(0)
        if visit[px][py]==0:
            visit[px][py]=1
        base[px][py] = cnt
        # for row in base:
        #     print(row)
        # print()
        for i in range(4):
            nx = px+dx[i]
            ny = py+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                if (nx,ny) in stack:
                    p = stack.index((nx,ny))
                    if stack2[p] > cnt+1:
                        stack2[p] = cnt+1
                else:
                    stack.append((nx,ny))
                    stack2.append(cnt+1)

    for a in visit:
        if 0 in a:
            cnt=-1
            break
    for i in range(N):
        for j in range(N):
            if base[i][j]!='-':
                base[i][j]=0
                visit[i][j]=0
    return cnt

N, M = map(int, input().split())

base = [list(map(int,input().split()))for _ in range(N)]
visit=[[0 for _ in range(N)]for _ in range(N)]

s_point = []
for i in range(N):
    for j in range(N):
        if base[i][j]==2:
            s_point.append((i,j))
        elif base[i][j]==1:
            base[i][j] = '-'
            visit[i][j] = 1

case = []
l = len(s_point)

for i in range(1<<l):
    temp = []
    for j in range(l+1):
        if i & (1<<j):
            temp.append(s_point[j])
    if len(temp) == M:
        case.append(temp)

result = []
for i in case:
    # check(i)
    a = check(i)
    if a!=-1:
        result.append(a)

if len(result)!=0:
    print(min(result))
else:
    print(-1)