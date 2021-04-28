arr = []
times = 1

for i in range(3):
    arr.append(int(input()))
    times = times * arr[i]
times = str(times)

for i in range(10):
    cnt = 0
    for j in range(len(times)):
        if(ord(times[j]) == (i + 48)):
            cnt += 1
    print(cnt)
