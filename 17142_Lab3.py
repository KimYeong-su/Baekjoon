dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(arr):
    global minimum
    stack = []
    stack2 = []

    for a in arr:
        stack.append(tuple(a))
        stack2.append(0)
    while len(stack)!=0:
        # if stack2[-1] > minimum:
        #     break
        x,y=stack.pop(0)
        cnt=stack2.pop(0)

        base[x][y] = cnt
        visit[x][y]=1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                if (nx,ny) not in stack:
                    stack.append((nx,ny))
                    stack2.append(cnt+1)
                else:
                    if stack2[stack.index((nx,ny))] > cnt+1:
                        stack2[stack.index((nx,ny))] = cnt+1
        if minimum<cnt+1:
            break
    # print(cnt)
    # for row in base:
    #     print(row)
    # print()


    for i in visit:
        if 0 in i:
            cnt = -1
            break

    for i in range(N):
        for j in range(N):
            if base[i][j]==0:
                base[i][j]='*'
            elif base[i][j]=='-' or base[i][j]=='*':
                continue
            else:
                # base[i][j]=0
                visit[i][j]=0
    return cnt

N, M = map(int,input().split())

base = [list(map(int,input().split()))for _ in range(N)]
visit = [[0 for _ in range(N)]for _ in range(N)]

start = []
for i in range(N):
    for j in range(N):
        if base[i][j]==1:
            visit[i][j]=1
            base[i][j]='-'
        elif base[i][j]==2:
            start += [(i,j)]
            base[i][j]='*'
            visit[i][j]=1

l = len(start)
case = []
for i in range(1<<l):
    temp = []
    for j in range(l+1):
        if i & (1<<j):
            temp += [start[j]]
    if len(temp)==M:
        case += [temp]
minimum = 10000
for i in case:
    a = check(i)
    if a != -1:
        if minimum > a:
            minimum = a

if minimum==10000:
    print(-1)
else:
    print(minimum)

'''
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(arr):
    global minimum
    stack = []
    stack2 = []

    for a in arr:
        x,y = a
        stack.append((x,y))
        stack2.append(0)
    while len(stack)!=0:
        # if stack2[-1] > minimum:
        #     break
        x,y=stack.pop(0)
        cnt=stack2.pop(0)

        base[x][y] = cnt
        visit[x][y]=1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                if (nx,ny) not in stack:
                    stack.append((nx,ny))
                    stack2.append(cnt+1)
                else:
                    if stack2[stack.index((nx,ny))] > cnt+1:
                        stack2[stack.index((nx,ny))] = cnt+1
    print(cnt)
    for row in base:
        print(row)
    print()

    for i in visit:
        if 0 in i:
            cnt = -1
            break

    for i in range(N):
        for j in range(N):
            if base[i][j]!='-':
                # base[i][j]=0
                visit[i][j]=0
    return cnt

N, M = map(int,input().split())

base = [list(map(int,input().split()))for _ in range(N)]
visit = [[0 for _ in range(N)]for _ in range(N)]

start = []
for i in range(N):
    for j in range(N):
        if base[i][j]==1:
            visit[i][j]=1
            base[i][j]='-'
        elif base[i][j]==2:
            start += [(i,j)]

l = len(start)
case = []
for i in range(1<<l):
    temp = []
    for j in range(l+1):
        if i & (1<<j):
            temp += [start[j]]
    if len(temp)==M:
        case += [temp]
minimum = 10000
for i in case:
    for j in start:
        if j not in i:
            base[j[0]][j[1]]='*'
            visit[j[0]][j[1]]=1
    a = check(i)
    if a != -1:
        if minimum > a:
            minimum = a

if minimum==10000:
    print(-1)
else:
    print(minimum)
    '''