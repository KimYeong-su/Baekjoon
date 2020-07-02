N = int(input())
result = [i for i in range(10)]
cnt = -1
while True:
    num = result.pop(0)
    cnt += 1
    if cnt == N:
        flag = True
        break
    for i in range(10):
        if i < num%10:
            temp = num*10 + i
            result.append(temp)
        else:
            break
    if not result:
        flag = False
        break
if flag:
    print(num)
else:
    print(-1)