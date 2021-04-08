import sys
input = sys.stdin.readline

base = {}
for i in range(4):
    base[i] = list(map(int, input().rstrip('\n')))
    
def rotation(gear_num, direction):
    if direction == 1:
        tmp = base[gear_num-1].pop(-1)
        base[gear_num-1] = [tmp] + base[gear_num-1]
    else:
        tmp = base[gear_num-1].pop(0)
        base[gear_num-1] += [tmp]

K = int(input().rstrip('\n'))
for _ in range(K):
    gear_num, direction = map(int, input().rstrip('\n').split())
    check=[False]*4
    check[gear_num-1]=True
    for idx in range(1,4):
        if 0<=gear_num-1-idx<4 and check[gear_num-idx]:
            if base[gear_num-idx-1][2] != base[gear_num-idx][6]:
                check[gear_num-1-idx] = True
        if 0<=gear_num+idx-1<4 and check[gear_num+idx-2]:
            if base[gear_num+idx-2][2] != base[gear_num+idx-1][6]:
                check[gear_num+idx-1] = True
    for i in range(4):
        if check[i]:
            if (gear_num-1)%2==i%2:
                rotation(i+1, direction)
            else:
                rotation(i+1, -direction)
answer = 0
for i in range(4):
    if base[i][0] == 1:
        answer += 2**i
print(answer)