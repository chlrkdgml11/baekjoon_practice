n = int(input())

b = []

for i in range(n):
    b.append(input())

def calculate(arr):
    cnt = 1
    sum = 0
    for i in range(len(arr)):
        if(arr[i] == 'O'):
            sum += cnt
            cnt += 1
        if(arr[i] == 'X'):
            cnt = 1
    return sum

for i in range(n):
    print(calculate(b[i]))
