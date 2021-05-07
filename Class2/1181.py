arr = []

N = int(input())

for i in range(N):
    word = input()
    if word in arr:
        continue
    else:
        arr.append(word)    

arr.sort()

arr.sort(key = len)

for x in arr:
    print(x)
