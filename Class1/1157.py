a = input().upper()

b = []

for i in a:
    if i in b:
        continue
    b.append(i)

c = [0 for col in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if(b[i] == a[j]):
            c[i] += 1

if c.count(max(c)) > 1:
    print('?')
else:
    print(b[c.index(max(c))])
