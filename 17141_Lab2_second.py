def check(arr):
    maximum = 0
    for i in range(N):
        for j in range(N):
            temp = 10000
            if (i,j) not in arr and base[i][j]!='-':
                for a in arr:
                    x,y = a
                    cnt = abs(i-x)+abs(j-y)
                    if temp>cnt:
                        temp = cnt
                if maximum<temp:
                    maximum = temp
    return maximum


N, M = map(int, input().split())

base = [list(map(int,input().split()))for _ in range(N)]

s_point = []
for i in range(N):
    for j in range(N):
        if base[i][j]==2:
            s_point.append((i,j))
        elif base[i][j]==1:
            base[i][j] = '-'
case = []
l = len(s_point)

for i in range(1<<l):
    temp = []
    for j in range(l+1):
        if i & (1<<j):
            temp.append(s_point[j])
    if len(temp) == M:
        case.append(temp)

minimum = 10000
for i in case:
    # check(i)
    result=check(i)
    if minimum > result:
        minimum = result

print(minimum)