N = input().lower()

arr = [-1 for col in range(26)]

for i in N:
    if arr[ord(i)-97] == -1:
        arr[ord(i)-97] = N.index(i)

for i in range(26):
    print(arr[i], end=' ')
