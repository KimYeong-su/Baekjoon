def check(idx, d):
    g = float('inf')
    g1 = 0
    p = idx
    cnt = 0
    flag = True
    while True:
        p += d
        if 0<=p<n:
            ng = abs(buildings[idx]-buildings[p])/abs(idx-p)
            if buildings[idx]<buildings[p]:
                if ng>g1:
                    cnt += 1
                    g1 = ng
                    flag = False
            else:
                if ng<g and flag:
                    cnt += 1
                    g=ng
        else:
            return cnt


n = int(input())
buildings = list(map(int,input().split()))

result = 0
for i in range(n):
    temp = 0
    temp += check(i,-1)
    temp += check(i, 1)
    if result < temp:
        result = temp
print(result)
