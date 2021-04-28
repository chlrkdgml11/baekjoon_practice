a = []

for i in range(10):
    a.append(int(input()))

b = []
count = 0
for i in range(10):
    if a[i] % 42 not in b:
        count += 1
        b.append(a[i] % 42)

print(count)
