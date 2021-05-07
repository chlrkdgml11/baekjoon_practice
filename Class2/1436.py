N = int(input())

cnt = 0
for i in range(1, 10000667):
    i = str(i)
    if(i.count('666')):
        cnt += 1
    if(cnt == N):
        print(i)
        break