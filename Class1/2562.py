arr = [0 for col in range(9)]

for i in range(9):
    arr[i] = int(input())

print(max(arr))
print(arr.index(max(arr)) + 1)