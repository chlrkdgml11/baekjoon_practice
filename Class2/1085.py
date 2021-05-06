x, y, w, h = map(int, input().split())

arr = [x, w-x, h-y, y]

print(min(arr))
