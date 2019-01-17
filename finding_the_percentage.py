cube = lambda x: x ** 3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        cur_list = fibonacci(n - 1)
        return cur_list + [cur_list[-2] + cur_list[-1]]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
