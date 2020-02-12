N = int(input())
base = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for i in range(K):
    a, b = map(int, input().split())
    base[a-1][b-1]+=1
L = int(input())

method = []
for i in range(L):
    X, C = input().split()
    X = int(X)
    method.append((X,C))
method.append((10000,'N'))


a,b = 0,0
base[a][b] = 2
dx = [-1,0,1,0]
dy = [0,1,0,-1]
i = 0
j = 1
flag = 1
times = 0
history = [(0,0)]
p=0
while i<len(method):
    t,D = method[i]
    for time in range(times+1,t+1):
        a += dx[j]
        b += dy[j]
        if a>=N or b>=N or a<0 or b<0:
            flag=0
            times = time
            break
        if base[a][b]==0:
            base[a][b]=2
            history.append((a,b))
            c,d = history[p]
            base[c][d]=0
            p+=1
        elif base[a][b]==1:
            base[a][b]=2
            history.append((a,b))
        elif base[a][b]==2:
            flag=0
            times = time
            break
        if time == t:
            if D == 'D':
                j +=1
                if j>3:
                    j=0
            elif D =='L':
                j-=1
                if j<0:
                    j=3
            times = t
    if flag==0:
        break
    i += 1

print(times)