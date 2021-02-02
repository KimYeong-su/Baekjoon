N, M = map(int, input().split())

woods = list(map(int, input().split()))

left = 0
right = max(woods)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for wood in woods:
        if wood > mid:
            cnt += wood - mid
    
    if cnt < M:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1

print(answer)