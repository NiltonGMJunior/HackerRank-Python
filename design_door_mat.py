if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    lines_top = []
    lines_bottom = []
    line_middle = 'WELCOME'.center(m, '-')
    pattern = '.|.'
    for i in range(n // 2):
        line = (pattern * (2 * i + 1)).center(m, '-')
        lines_top += [line]
        lines_bottom = [line] + lines_bottom
    door_mat = lines_top + [line_middle] + lines_bottom
    for line in door_mat:
        print(line)
    