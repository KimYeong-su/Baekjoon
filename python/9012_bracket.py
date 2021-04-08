import sys
input = sys.stdin.readline

N = int(input())
def check(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s==')':
            if not stack:
                return 'NO'
            else:
                stack.pop()
    if stack:
        return 'NO'
    return 'YES'

for _ in range(N):
    print(check(input()))