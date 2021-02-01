N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
search = list(map(int, input().split()))

for m in search:
    left = 0
    right = len(numbers)-1
    if numbers[right] == m or numbers[left] == m:
        print(1)
        continue
    flag = False
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == m:
            flag = True
            break
        elif numbers[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

    if flag:
        print(1)
    else:
        print(0)