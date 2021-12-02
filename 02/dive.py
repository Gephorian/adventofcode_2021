#!/usr/bin/env python3

with open('input.txt') as f:
    vectors = [ x.split() for x in f.readlines() ]

class Location():
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, direction, distance):
        if direction == 'forward':
            self.x += distance
        if direction == 'backward':
            self.x -= distance
        if direction == 'down':
            self.y += distance
        if direction == 'up':
            self.y -= distance

    @property
    def depth(self):
        return self.y

    @property
    def distance(self):
        return self.x

    @property
    def product(self):
        return self.x * self.y
    

def main():
    loc = Location()
    for direction, distance in vectors:
        loc.move(direction, int(distance))
    print(f'With a depth of {loc.depth} and having traveled a horizontal distance of {loc.distance}, the product is {loc.product}')

if __name__ == '__main__':
    main()
