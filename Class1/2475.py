array = list(map(int, input().split()))

sum = 0

for i in array:
    sum += i*i

print(sum % 10)
