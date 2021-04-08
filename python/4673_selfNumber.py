visit = [False] * 10000
visit[0] = True
def d(n):
    nn = n
    for i in str(n):
        nn += int(i)
    if nn < 10000 and not visit[nn]:
        visit[nn] = True
        d(nn)
    else:
        return
    
for i in range(1,10000):
    d(i)
for i in range(1,10000):
    if not visit[i]:
        print(i)