def sort_helper(n):
    ascending = "".join(sorted(str(n)))
    descending = "".join(sorted(str(n), reverse=True))
    return {"y": int(ascending), "x": int(descending)}


def count_digits(n):
    n = len(str(n))
    return int(n)


def decimal_to_base(d, b):
    digits = []
    while d > 0:
        digits.insert(0, str(d % b))
        d = d / b
    return "".join(digits)


def base_to_decimal(b, c):
    n = 0
    for d in str(b):
        n = c * n + int(d)
    return n


def get_diff(x, y, b):
    if b == 10:
        return int(x) - int(y)

    dx = base_to_decimal(x, b)
    dy = base_to_decimal(y, b)
    dz = dx - dy
    return decimal_to_base(dz, b)


def solution(n, b):
    arr = []
    while True:
        n_sorted = sort_helper(n)
        x = n_sorted["x"]
        j = n_sorted["y"]
        k = get_diff(x, j, b)

        k_len = count_digits(k)
        x_len = count_digits(x)
        if (k_len) != x_len:
            k = int(k) * pow(10, (x_len - k_len))

        for index, item in enumerate(arr):
            if item == k:
                return index + 1
        arr = [k] + arr
        n = k


print(solution("210022", 3))
