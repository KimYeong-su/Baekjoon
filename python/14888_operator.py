import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
base = list(map(int, input().rstrip('\n').split()))
visit = [False] * N
cnt_op = list(map(int, input().rstrip('\n').split()))
minimum = 1000000000
maximum = -1000000000
def dfs(idx,tmp):
    global maximum, minimum
    if idx==N:
        if tmp > maximum:
            maximum = tmp
        if tmp < minimum:
            minimum = tmp
        return
    for j in range(4):
        if cnt_op[j] > 0:
            cnt_op[j] -= 1
            if j == 0:
                dfs(idx+1,tmp+base[idx])
            elif j == 1:
                dfs(idx+1,tmp-base[idx])
            elif j == 2:
                dfs(idx+1,tmp*base[idx])
            else:
                if tmp<0:
                    dfs(idx+1, -((-tmp)//base[idx]))
                else:
                    dfs(idx+1,tmp//base[idx])
            cnt_op[j] += 1

dfs(1,base[0])
print(maximum)
print(minimum)