n = 0
result1, result = 0, 0
arr = list(range(1, 101))

for i in range(1, 51):
    result1 = arr[n] + arr[n+1]
    result = result + result1
    n = n+2

print(result)
