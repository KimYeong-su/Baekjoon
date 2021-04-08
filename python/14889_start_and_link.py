def f(index,A,B):
    global minimum
    if index==N:
        temp = 0
        for a in range(N//2):
            for b in range(a+1,N//2):
                temp += sinergy[A[a]][A[b]]+sinergy[A[b]][A[a]]
                temp -= sinergy[B[a]][B[b]]+sinergy[B[b]][B[a]]
        if minimum > abs(temp):
            minimum = abs(temp)
        return
    if len(A)<N//2:
        A.append(index)
        f(index+1,A,B)
        A.pop()
    if len(B)<N//2:
        B.append(index)
        f(index+1,A,B)
        B.pop()

N = int(input())

sinergy = [list(map(int,input().split()))for _ in range(N)]
minimum = 200000
f(1,[0],[])

print(minimum)
