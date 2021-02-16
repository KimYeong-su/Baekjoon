import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]
lines.sort()
left = 0
right = lines[-1] * 2

answer = 0
while left <= right:
    cnt= 0
    mid = (left + right) // 2
    for line in lines:
        cnt += line//mid

    if cnt < N:
        right = mid - 1
    else:
        if mid > answer:
            answer = max(answer,mid)
        left = mid + 1
print(answer)
