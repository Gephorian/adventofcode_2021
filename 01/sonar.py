#!/usr/bin/env python3

with open('input.txt') as f:
    measurements = [ int(x) for x in f.readlines() ]

# Part 1
increases = 0
# Start at index 1 to compare to the first value
for n in range(1, len(measurements)):
    if measurements[n] > measurements[n - 1]:
        increases += 1
print(f'Part 1: {increases}')

# Part 2
increases = 0
previous = 0
for n in range(3, len(measurements)):
    sampleSum = sum(measurements[n-3:n])
    if sampleSum > previous:
        increases += 1
    previous = sampleSum
print(f'Part 2: {increases}')
