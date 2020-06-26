def check(temp,cnt,idx):
    global result
    if temp == want:
        if result > cnt:
            result = cnt
        return
    if cnt > result:
        return
    if want[idx] == q[0]:
        temp.append(q.pop(0))
        check(temp,cnt,idx+1)
        q.insert(0,temp.pop())
    else:
        if q.index(want[idx])<len(q)//2+1:
            q.append(q.pop(0))
            check(temp,cnt+1,idx)
            q.insert(0,q.pop())
        else:
            q.insert(0,q.pop())
            check(temp,cnt+1,idx)
            q.append(q.pop(0))


N, M = map(int,input().split())
q = [i for i in range(1,N+1)]
want = list(map(int,input().split()))
result = float('inf')
check([],0,0)
print(result)