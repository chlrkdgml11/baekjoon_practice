K, N = map(int, input().split())

arr = []

for i in range(K):
    arr.append(int(input()))

cnt = 0
cm = (1 + max(arr)) // 2

while(cnt != N):
    cnt = 0
    for i in range(K):
        cnt += arr[i] // cm

    if(cnt == N):
        break

    if(cnt > N):
        cm = (cm + max(arr)) // 2

    elif(cnt < N):
        cm = cm // 2

print(cm)
