import sys
import heapq

N, M = map(int,sys.stdin.readline().split())
true = list(map(int,sys.stdin.readline().split()))
check = set(true[1:])

party = []
for _ in range(M):
    tmp = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(party,[-tmp[0], tmp[1:]])

if len(check) == 0:
    print(M)
    exit()

answer = 0
while True:
    once = []
    for a in party:
        _, tmp = a

        for i in tmp:
            if i in check:
                check.update(tmp)
                break
        else:
            heapq.heappush(once,a)
    if once == party:
        break
    else:
        party = once

print(len(party))