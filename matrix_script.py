#!/bin/python3

import math
import os
import random
import re
import sys

def decode_string(string):
    pattern = re.compile(r'(\w)(\W+)(\w)')
    repl = r'\1 \3'
    return re.sub(pattern, repl, string)


def decode_matrix(matrix):
    output = ''
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            output += matrix[j][i]
    return output

# IMPORTANT NOTICE: When submitting this code on Hackerrank, the if __name__ == "__main__": line should be ommited because the solution won't accept any if statements in the code 

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    print(decode_string(decode_matrix(matrix)))