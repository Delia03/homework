arr = [9, 8, 6, 4, 5, 1, 3, 10]


# 冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


# bubbleSort(arr)

# 选择排序
def selectSort(arr):
    n = len(arr)
    for i in range(n):
        min_idex = i
        for j in range(i + 1, n):
            if arr[min_idex] > arr[j]:
                min_idex = j
        arr[i], arr[min_idex] = arr[min_idex], arr[i]
    print(arr)


# selectSort(arr)

def is_palindromic(stra):
    middle_index = len(stra) // 2
    if stra[:middle_index] == stra[middle_index:][::-1]:
        print("是回文")
    else:
        print("不是回文")


# is_palindromic("abccba")

def is_palindromic2(stra):
    return stra == stra[::-1]


# print(is_palindromic2("abccb"))


def get_info():
    name = "lili"
    age = 10
    return name, age


def log(fuction):
    def wrap(*args, **kw):
        print("do {}".format(fuction.__name__))
        fuction(*args, **kw)
        print("finish")

    return wrap


@log
def add(x, y):
    print("{}+{}={}".format(x, y, x + y))


add(3, 4)
