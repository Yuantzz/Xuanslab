arr = input("输入数组").split()
arr = [int(x) for x in arr]


def bubble_sort(arr):
    n = len(arr)

    # 外层循环控制需要比较的轮数
    for i in range(n - 1):

        # 内层循环在当前轮数中比较相邻的元素
        # 并交换顺序不对的元素
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


sorted_arr = bubble_sort(arr)
print(sorted_arr)
