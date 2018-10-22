#!/bin/python3

N = int(input())

if N % 2 != 0:
    output = 'Weird'
elif N in range(2, 6):
    output = 'Not Weird'
elif N in range(6, 21):
    output = 'Weird'
else:
    output = 'Not Weird'

print(output)
