X = int(input())
sticks = [64]
while sum(sticks)!=X:
    if sum(sticks) > X:
        stick = sticks.pop(len(sticks)-1)
        temp = stick//2
        sticks.append(temp)
        if sum(sticks) < X:
            sticks.append(temp)
print(len(sticks))