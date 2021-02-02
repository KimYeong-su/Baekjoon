N = int(input())
answer = 0
for n in range(N,0,-1):
    tmp = str(n)
    if len(tmp) < 3:
        answer += 1
        continue
    d = int(tmp[0]) - int(tmp[1])
    for i in range(1,len(tmp)-1):
        if int(tmp[i]) - int(tmp[i+1]) != d:
            break
    else:
        answer += 1
print(answer)