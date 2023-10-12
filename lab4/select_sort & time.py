import random
import time

n = int(input("请输入数组长度: "))
m = int(input("请输入数组范围: "))
time_start = time.time()


def generate_random_array(arr, n, m):
    for i in range(n):
        arr[i] = random.randint(0, m - 1)


arr = [0] * n
generate_random_array(arr, n, m)


def select_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array


sorted_arr = select_sort(arr)
time_end = time.time()
sum_time = time_end - time_start

print('time cost', sum_time, 's')
print(sorted_arr)
