N = int(input())
friends = {}
for i in range(N):
    temp = list(input())
    for j in range(N):
        if temp[j]=='N': continue
        if i in friends.keys():
            friends[i] += [j]
        else:
            friends[i] = [j]
result = 0
for key in friends.keys():
    temp = set()
    for k in friends[key]:
        if k != key:
            temp.add(k)
        for k1 in friends[k]:
            if k1 != key:
                temp.add(k1)
    if len(temp) > result:
        result = len(temp)
print(result)