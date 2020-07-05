'''
1003_피보나치 함수
sol) 피보나치 함수는 재귀기 때문에 maximum 40이란 값은 너무 많은 시간이 걸립니다.
따라서 피보나치의 구조와 마찬가지로 0과 1이 return되는 횟수는
주어진 n 보다 n-1, n-2 된 값들의 0, 1 return 횟수의 합과 같은 점을 이용해서
간단하게 for문을 돌려 풀었습니다.
'''
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        result0 = [1, 0]
        result1 = [0, 1]
        for i in range(2,n+1):
            result0 += [sum(result0[i-2:i])]
            result1 += [sum(result1[i-2:i])]
        print(result0[n], result1[n])