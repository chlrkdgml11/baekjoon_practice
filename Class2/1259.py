arr = []
while(1):
    a = input()
    if(a == '0'):
        break
    arr.append(a)

for x in arr:
    cnt = 0
    for l in range(int(len(x) / 2) + 1):
        if(x[l] != x[len(x) - 1 - l]):
            cnt += 1
    if(cnt == 0):
        print('yes')
    else:
        print('no')