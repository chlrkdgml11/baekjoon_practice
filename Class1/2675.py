n = int(input())

count = []
string = []

for i in range(n):
    a, b = map(str, input().split())
    count.append(a)
    string.append(str(b))

for i in range(n):
    for j in range(len(string[i])):
        for k in range(int(count[i])):
            print(string[i][j], end='')
    print('')
