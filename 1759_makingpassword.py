import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpa = list(input().split())
alpa.sort()
answer = []
def password(length, visit, tmp, now):
    global answer
    if length == L:
        tmp1 = 0 
        tmp2 = 0
        for w in tmp:
            if w in ['a', 'e', 'i', 'o', 'u']:
                tmp1 += 1
            else:
                tmp2 += 1
            if tmp1 > 0 and tmp2 > 1:
                answer.append(tmp)
                return
        return
    for i in range(now,C):
        if visit[i]: continue
        visit[i] = True
        password(length+1, visit, tmp+alpa[i], i+1)
        visit[i] = False

visit = [0] * C
password(0, visit, '', 0)
for word in answer:
    print(word)