'''
백준 1083번_소트
sol) 버블소팅을 사용하는것은 맞지만 맨 앞을 가장 큰 수로 고정시키게 사용!
뒤부터 하면 안되요~ 그러면 문제에서 이야기하는 사전순으로 가장 뒷서는 것이 아니기 때문..
요거 땜시.. 이틀을 고민 했네..ㅠㅜ 문제를 잘 읽읍시다.
'''

from sys import stdin

input = stdin.readline

N = int(input())
base = list(map(int, input().split()))
S = int(input())

temp = list(sorted(base, reverse=True))
for i in range(N-1):
    if S == 0:
        break
    maximum, idx = base[i], i
    if maximum == max(base[i:]): continue # 이걸 추가했는데 오히려 시간이 더 걸리네? 허허..
    for j in range(i+1,min(N, i+S+1)):
        if maximum < base[j]:
            maximum = base[j]
            idx = j
    S -= idx - i
    base[i+1:idx+1] = base[i:idx]
    base[i] = maximum

result = ' '.join(map(str, base))
print(result)