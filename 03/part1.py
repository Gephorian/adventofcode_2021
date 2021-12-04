#!/usr/bin/env python3
with open('input.txt') as f:
    readings = [ x.strip() for x in f.readlines() ]

def most_bits(List):
    return max(set(List), key = List.count)

def least_bits(List):
    return min(set(List), key = List.count)

rows = []
for i in range(len(readings[0])):
    rows.append(''.join([ x[i] for x in readings ]))

print(int(''.join([most_bits(x) for x in rows]),2) * int(''.join([least_bits(x) for x in rows]),2))
