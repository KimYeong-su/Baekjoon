'''
# https://inspirit941.tistory.com/200#recentEntries
# 중간 값을 찾기 위해 반은 최대힙을 반은 최소힙을 구현하여 최신화를 시켜준다.
# 짝수의 경우(최대, 최소 힙의 길이가 같은 경우) 더 작은 값을 출력하기 때문에 항상 최대힙의 최대값을 출력해주면 된다.
'''

import sys, heapq
input = sys.stdin.readline

N = int(input())
max_heap, min_heap = [], []
answer = []
for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap,(num, num))

    if min_heap and min_heap[0][1] < max_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (max_value, max_value))
        heapq.heappush(max_heap, (-min_value, min_value))

    print(max_heap[0][1])