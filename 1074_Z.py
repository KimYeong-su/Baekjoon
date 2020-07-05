'''
1074_Z
sol) col과 row의 나머지를 통해 어느만큼의 값이 더해져야하는지를 판단
또한 가장 큰 사각형에서 점점 작아질 수록 4의 배수로 나눠진다는 것을 생각!!
정사각형의 넓이는 길이의 제곱의 비례 한다는 거.. 이걸 놓치면 힘듭니다.
진짜 코드를 더럽게 짰는데 각각의 row는 2의 배수로 커지고 col은 1씩 커진다는 점을 생각해
그냥 2진수로 바꿔서 자리마다의 크기를 이용한다면 단 2줄로 풀수 있다는 점.. 
'''

def z_potition(size, tr, tc, result):
    global answer
    if size==0:
        answer = result
        return
    if tr < 2**(size-1) and tc < 2**(size-1):
        z_potition(size-1, tr%2**(size-1), tc%2**(size-1), result+4**(size-1)*0)
    elif tr < 2**(size-1) and tc >= 2**(size-1):
        z_potition(size-1, tr%2**(size-1), tc%2**(size-1), result+4**(size-1)*1)
    elif tr >= 2**(size-1) and tc < 2**(size-1):
        z_potition(size-1, tr%2**(size-1), tc%2**(size-1), result+4**(size-1)*2)
    elif tr >= 2**(size-1) and tc >= 2**(size-1):
        z_potition(size-1, tr%2**(size-1), tc%2**(size-1), result+4**(size-1)*3)
    
N, r, c = map(int,input().split())
answer = 0
z_potition(N, r, c, 0)
print(answer)

# n,r,c=map(int,input().split())
# print(int(f'{c:b}',4)+2*int(f'{r:b}',4))