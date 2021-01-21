num = int(input())

for i in range(1, 1000000):
    base = str(i)
    tmp = num
    for j in list(base):
        tmp -= int(j)
    if tmp == i:
        print(i)
        exit()
print(0)