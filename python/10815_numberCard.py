N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
search = list(map(int,input().split()))
answer = []
for s in search:
    left = 0
    right = N-1
    flag = False
    if numbers[left] == s or numbers[right] == s:
        answer.append(1)
        continue
    while left <= right and not flag:
        mid = (left + right) // 2
        if s == numbers[mid]:
            flag = True
        elif s < numbers[mid]:
            right = mid-1
        else:
            left = mid+1

    if flag:
        answer.append(1)
    else:
        answer.append(0)

print(' '.join(map(str, answer)))