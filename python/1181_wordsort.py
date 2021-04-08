import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    word = input()
    words.add((len(word),word[:-1]))

words = sorted(list(words))
for word in words:
    print(word[1])