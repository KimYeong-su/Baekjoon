import heapq

def Dijkstra(s):
    pq = []
    key = [float('inf')]*n
    key[s] = 0
    visit = [False]*n
    heapq.heappush(pq,[0,s])
    while pq:
        k,x = heapq.heappop(pq)
        if visit[x]: continue
        visit[x] = True
        for i in temp[x]:
            y, k = i
            key[y] = min(key[y], key[x]+k)
        heapq.heappush(pq,[key[y],y])
    return key

def check(s,cnt,flag,history,num):
    global result
    if False not in visit2.values() and flag:
        if result > cnt:
            result = cnt
        return
    if result < cnt: return
    if not flag:
        if not visit1[0]: visit1[0] = True
        for end, weight in g[s]:
            if end==n-1 and False in list(visit1.values())[:n-1]: continue
            if visit1[end]: continue
            visit1[end] = True
            if False in visit1.values():
                history.append(end)
                check(end, cnt+weight, 0, history, num)
                history.pop()
            else:
                history.append(end)
                check(end,cnt+weight, 1, history, num)
                history.pop()
            visit1[end] = False
    if flag:
        if not visit2[n-1]: visit2[n-1] = True
        for end, weight in g[s]:
            if end==0 and False in list(visit2.values())[1:]: continue
            if visit2[end]: continue
            if end not in history[:h] and num<h: continue
            visit2[end] = True
            check(end, cnt+weight, 1, history, num+1)
            visit2[end] = False

for tc in range(1,3):
    n, m = map(int,input().split())
    h = (n-1)//2
    temp = {}
    g = {}
    for _ in range(m):
        u, v, t = map(int,input().split())
        if u not in temp:
            temp[u] = [(v,t)]
        else:
            temp[u] += [(v,t)]
        if v not in temp:
            temp[v] = [(u,t)]
        else:
            temp[v] += [(u,t)]
    for i in range(n):
        temp1 = Dijkstra(i)
        for idx,j in enumerate(temp1):
            if j!=0:
                if i not in g:
                    g[i] = [(idx,j)]
                else:
                    g[i] += [(idx,j)]
    visit1 = {}
    visit2 = {}
    for i in range(n):
        visit1[i] = False
        visit2[i] = False
    
    result = float('inf')
    check(0,0,0,[],0)
    print('Case {}: {}'.format(tc,result))