def print_formatted(number):
    lines = []
    for i in range(number):
        num_dec = str(i + 1)
        num_oct = oct(i + 1)[oct(i + 1).index('o') + 1 : ]
        num_hex = hex(i + 1)[hex(i + 1).index('x') + 1 : ].upper()
        num_bin = bin(i + 1)[bin(i + 1).index('b') + 1 : ]

        line = [num_dec, num_oct, num_hex, num_bin]
        lines.append(line)
    
    width = len(lines[-1][-1])

    output = []
    for line in lines:
        output.append(" ".join([string.rjust(width) for string in line]))
    
    print("\n".join([line for line in output]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)