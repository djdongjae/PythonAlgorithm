def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a == None:
        return 0
    b = last(n, array, x, 0, n - 1)
    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] < target:
            return first(array, target, mid + 1, end)
        else:
            return first(array, target, start, mid - 1)


def last(n, array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
            return mid
        elif array[mid] < target:
            return last(n, array, target, mid + 1, end)
        else:
            return last(n, array, target, start, mid - 1)


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == None:
    print(-1)
else:
    print(count)