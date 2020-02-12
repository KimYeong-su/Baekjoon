s = input()
cnt=1
for i in range(len(s)):
    if s[i] == ' ':
        cnt+=1
if s[0]==' ':
    cnt -= 1
if s[-1]==' ':
    cnt -= 1
print(cnt)