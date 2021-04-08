N, M = map(int, input().split())
base = [list(map(str,input())) for _ in range(N)]
case = [['W', 'B','W', 'B','W', 'B','W', 'B'], ['B','W','B','W','B','W','B','W']]
answer = float('inf')
for i in range(2):
    for r in range(N-7):
        tmp_b = 0
        tmp_w = 0
        for c in range(M-7):
            if case[(r+i)%2][c%2] == base[r][c:c+8]: continue
            for k in range(8):
                if case[(r+i)%2][k] == base[r][k]: continue
                if base[r][k] == 'B':
                    tmp_b += 1
                else:
                    tmp_w += 1
        print(tmp_b, tmp_w)
        # answer = min(answer, tmp_b, tmp_w)
# print(answer)    