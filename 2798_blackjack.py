from sys import stdin

N, M = map(int,stdin.readline().split())
base = list(map(int, stdin.readline().split()))
answer = 0
for i in range(len(base)-2):
    tmp = base[i]
    if tmp > M: continue
    for j in range(i+1,len(base)-1):
        tmp += base[j]
        if tmp > M:
            tmp -= base[j]
            continue
        for k in range(j+1, len(base)):
            tmp += base[k]
            if tmp > M:
                tmp -= base[k]
                continue
            answer = max(answer, tmp)
            tmp -= base[k]
        tmp -= base[j]

print(answer)