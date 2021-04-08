from itertools import combinations

N, M = map(int,input().split())
home = []
store = []
length = {}
for i in range(1,N+1):
    temp = list(map(int,input().split()))
    for j in range(1,N+1):
        if temp[j-1]==1:
            home.append((i,j))
            length[(i,j)] = float('inf')
            continue
        if temp[j-1]==2:
            store.append((i,j))

case = list(combinations(store, M))
result = float('inf')
for c in case:
    for i in range(M):
        for h in home:
            temp = abs(c[i][0]-h[0])+abs(c[i][1]-h[1])
            if length[h] > temp:
                length[h] = temp
    if sum(length.values()) < result:
        result = sum(length.values())
    for k in length.keys():
        length[k] = float('inf')
print(result)