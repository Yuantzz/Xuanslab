n = 0
arr = list(range(1, 101))

for i in range(0, 100):
    if arr[n] % 2 == 1:
        print(arr[n], end=" ")
    n = n+1
