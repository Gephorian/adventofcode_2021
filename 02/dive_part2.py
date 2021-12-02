#!/usr/bin/env python3
from dive import Location

with open('input.txt') as f:
    vectors = [ x.split() for x in f.readlines() ]

class aim(Location):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def move(self, direction, distance):
        if direction == 'forward':
            self.x += distance
            self.y += distance * self.aim
        if direction == 'down':
            self.aim += distance
        if direction == 'up':
            self.aim -= distance

def main():
    loc = aim()
    for direction, distance in vectors:
        loc.move(direction, int(distance))
    print(f'With a depth of {loc.depth} and having traveled a horizontal distance of {loc.distance}, the product is {loc.product}')

if __name__ == '__main__':
    main()
