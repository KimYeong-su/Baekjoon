N = int(input())

cnt = -1
result = [i for i in range(10)]

while result:
    num = result.pop(0)
    cnt += 1
    if cnt == N:
        print(num)
        exit()
    for i in range(10):
        if num%10 <= i: break
        result.append(num*10 + i)
print(-1)