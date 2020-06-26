def dfs(cnt):
    global result, number
    if number==0:
        if result > cnt:
            result = cnt
        return
    if cnt > result:
        return
    for r in range(10):
        for c in range(10):
            if base[r][c]:
                for k in range(4,-1,-1):
                    if r+k<10 and c+k<10 and papers[k]<5:
                        for x in range(r,r+k+1):
                            if 0 in base[x][c:c+k+1]:
                                break
                            if x==r+k:
                                for y in range(r,r+k+1):
                                    base[y][c:c+k+1] = [0]*(k+1)
                                papers[k] += 1
                                number -= 1
                                dfs(cnt+1)
                                number += 1
                                papers[k] -= 1
                                for y in range(r,r+k+1):
                                    base[y][c:c+k+1] = [1]*(k+1)


base = [list(map(int,input().split()))for _ in range(10)]
papers = {}
result = float('inf')
number = 0
for i in range(10):
    for j in range(10):
        if base[i][j]:
            number+=1
for i in range(5):
    papers[i]=0
dfs(0)
if result==float('inf'):
    print(-1)
else:
    print(result)