def get_fibonacci_number(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def get_stingy(n):
    if n == 1:
        return 1
    stingy_list = []
    for i in range(1, n):
        if get_fibonacci_number(i) <= n and sum(stingy_list) < n:
            stingy_list.append(get_fibonacci_number(i))
        else:
            break
    if sum(stingy_list) > n:
        stingy_list.pop()

    return len(stingy_list)

def get_generous(n):
    generous_list = [1]
    if n > 1:
        for i in range(2, n):
            if sum(generous_list) < n:
                generous_list.append(generous_list[i-2] * 2)
            else:
                break
        if sum(generous_list) > n:
            generous_list.pop()

    return len(generous_list)

def get_solution(n):
    return abs(get_stingy(n) - get_generous(n))

def solution(total_lambs):
    return get_solution(total_lambs)

print(solution(143))