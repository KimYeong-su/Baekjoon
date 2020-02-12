s = list(input())
result = []

for i in s:
    if 96<ord(i)<123:
        result.append(ord(i)-32)
    else:
        result.append(ord(i))

n = len(set(result))
counting = [0 for _ in range(26)]

for i in range(len(s)):
    counting[result[i]-65] += 1

cnt=0
for i in counting:
    if max(counting) == i:
        cnt += 1

if cnt != 1:
    print('?')
else:
    print(chr(counting.index(max(counting))+65))