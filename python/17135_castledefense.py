def defense(i,j,k):
    cnt =0
    line = 0
    arr = [[0 for _ in range(M)]for _ in range(N)]
    for a in range(N):
        for b in range(M):
            arr[a][b] = base[a][b]
    while line<N:
        temp = []
        for archor in (i, j, k):
            minD = D*2
            ti = -1
            tj = -1
            for a in range(N-1,-1,-1):
                for b in range(M):
                    if arr[a][b]==1 and (abs(N-a)+abs(archor-b))<=D:
                        if minD>(abs(N-a)+abs(archor-b)):
                            minD = abs(N-a)+abs(archor-b)
                            ti, tj = a,b
                        elif minD==(abs(N-a)+abs(archor-b)):
                            if tj > b:
                                ti, tj = a,b
            temp.append((ti,tj))

        for p in range(3):
            si,sj = temp[p]
            if arr[si][sj]==1 and si != -1 and sj != -1:
                arr[si][sj]=0
                cnt+=1
        if zero == arr:
            return cnt
        arr.pop()
        arr.insert(0,[0]*M)
        line+=1
    return cnt


N, M, D = map(int,input().split())

base = [list(map(int,input().split())) for _ in range(N)]
zero = [[0 for _ in range(M)]for _ in range(N)]

maximum = 0
for i in range(0, M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            result=defense(i,j,k)
            if maximum<result:
                maximum = result
print(maximum)