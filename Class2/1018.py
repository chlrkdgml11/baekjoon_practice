a, b = map(int, input().split())

arr = []
board_01 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
board_02 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

result = 9999
for i in range(a):
    arr.append(input())


for i in range(a-7):
    for j in range(b-7):
        sum = 0
        sum_01 = 0
        sum_02 = 0
        for x in range(8):
            for y in range(8):
                if(arr[i+x][j+y] != board_01[x][y]):
                    sum_01 += 1
                if(arr[i+x][j+y] != board_02[x][y]):
                    sum_02 += 1
            
        if(sum_01 >= sum_02):
            sum = sum_02
        else:
            sum = sum_01
        if(result > sum):
            result = sum

print(result)
