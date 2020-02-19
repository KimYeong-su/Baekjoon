def defense(i,j,k):
    cnt =0
    minD = D+1
    temp = []
    for archor in (i, j, k):
        ti = -1
        tj=-1
        for a in range(N-1,-1,-1):
            for b in range(M):
                if abs(N-a)+abs(archor-b)<=D and base[a][b]==1:
                    if minD>abs(N-a)+abs(archor-b):
                        minD = abs(N-a)+abs(archor-b)
                        ti, tj = a,b
        temp.append((ti,tj))
    for i in range(3):
        si,sj = temp[i]
        if base[si][sj]==1:
            base[si][sj]=0
            for row in base:
                print(row)
            print()
            cnt+=1
    return cnt


N, M, D = map(int,input().split())

base = [list(map(int,input().split())) for _ in range(N)]

maximum = 0

for i in range(0, M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            result=defense(i,j,k)
            if maximum<result:
                maximum = result
print(maximum)
