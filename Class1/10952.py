a = []
while(True):
    x, y = map(int, input().split())
    if(x == 0 and y == 0):
        break
    a.append(x)
    a.append(y)

for i in range(0, int(len(a)), 2):
    print(a[i]  + a[i+1])
