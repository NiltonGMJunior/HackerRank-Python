if __name__ == '__main__':
    n = int(input())
    output = [i**2 for i in range(n) if i >= 0]
    for element in output:
        print(element)
