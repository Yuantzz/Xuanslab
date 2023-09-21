arr = input("输入数组:").split()
arr = [int(x) for x in arr]
m = 0
n = len(arr)
for i in range(n-1):
    arr[n-1], arr[m] = arr[m], arr[n-1]
    m = m+1
    n = n-1

print(arr)
