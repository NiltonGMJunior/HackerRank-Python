import textwrap

# My solution without textwrap (works fine)
# def wrap(string, max_width):
#     lines = []
#     total_length = 0
#     for i in range(len(string) // max_width):
#         lines.append(string[i * max_width : (i + 1) * max_width])
#         total_length += max_width
#     if total_length != max_width:
#         lines.append(string[max_width * (len(string) // max_width) : ])
#     return "\n".join(lines)

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)