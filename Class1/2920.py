N = input().split()

for i in range(8):
    N[i] = int(N[i])

result_ascending = sorted(N)
result_descending = sorted(N, reverse=True)

if(result_ascending == N):
    print('ascending')
elif(result_descending == N):
    print('descending')
else:
    print('mixed')
    