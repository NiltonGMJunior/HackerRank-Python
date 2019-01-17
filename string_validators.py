if __name__ == '__main__':
    s = input()
    outputs = [False] * 5
    for char in s:
        if all(outputs):
            break
        if char.isalnum():
            outputs[0] = True
        if char.isalpha():
            outputs[1] = True
        if char.isdigit():
            outputs[2] = True
        if char.islower():
            outputs[3] = True
        if char.isupper():
            outputs[4] = True
    for output in outputs:
        print(output)