n = int(input())

score = list(map(int, input().split()))

M = max(score)

sum = 0
for i in score:
    i = i / M * 100
    sum += i

print(sum / n)
