s = int(input())
base = list(map(int,input().split()))
T = int(input())
method = []
a,b = 0,-1
for i in range(T):
    method.append(tuple(map(int,input().split())))

for i in range(len(method)):
    sex, number = method[i]
    if sex == 1:
        for j in range(1,(s//number)+1):
            if base[j*number-1] == 1:
                base[j*number-1] = 0
            else:
                base[j*number-1] = 1
    else:
        for j in range(51):
            if number-j-1>=0 and number+j-1<len(base):
                if base[number-j-1] == base[number+j-1]:
                    a = number-j-1
                    b = number+j-1
                else:
                    break
        for k in range(a,b+1):
            if base[k] == 1:
                    base[k] = 0
            else:
                    base[k] = 1

if s > 20:
    for i in range(1,(s//20)+1):
        print(' '.join(map(str,base[20*(i-1):20*i])))
        if i == s//20:
            print(' '.join(map(str,base[20*i:])))
else:
    print(' '.join(map(str,base)))