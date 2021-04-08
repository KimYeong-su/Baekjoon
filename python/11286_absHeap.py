import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    order = int(input())
    if order != 0:
        heapq.heappush(heap,(abs(order), order))
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])