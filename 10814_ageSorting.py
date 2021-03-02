import sys
input = sys.stdin.readline

N = int(input())
members = []
index = 0
for _ in range(N):
    age, name = input().split()
    members.append((int(age),index,name))
    index += 1
members.sort()
for member in members:
    print(str(member[0])+' '+member[2])