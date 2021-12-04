#!/usr/bin/env python3

class DiagnosticReport():
    def __init__(self, readings):
        self.readings = readings

    def most_bits(self, readings):
        rows = []
        for i in range(len(readings[0])):
            rows.append(''.join([ x[i] for x in readings ]))
        return ''.join([self.most(x) for x in rows]) 

    def least_bits(self, readings):
        rows = []
        for i in range(len(readings[0])):
            rows.append(''.join([ x[i] for x in readings ]))
        return ''.join([self.least(x) for x in rows]) 
        
    @staticmethod
    def most(List):
        if List.count('0') == List.count('1'):
            return "1"
        return max(set(List), key = List.count)

    @staticmethod
    def least(List):
        if List.count('0') == List.count('1'):
            return "0"
        return min(set(List), key = List.count)

    @property
    def oxygen_rating(self):
        matches = self.readings
        index = 0
        while len(matches) > 1:
            for n in range(len(matches[0])):
                baseline = self.most_bits(matches)
                matches = [ x for x in matches if x[n] == baseline[n]]
        return int(matches[0],2)

    @property
    def scrubber_rating(self):
        matches = self.readings
        index = 0
        while len(matches) > 1:
            for n in range(len(matches[0])):
                baseline = self.least_bits(matches)
                    matches = [ x for x in matches if x[n] == baseline[n]]
        return int(matches[0],2)

    @property
    def life_support_rating(self):
        return self.scrubber_rating * self.oxygen_rating


if __name__ == '__main__':
    with open('input.txt') as f:
        readings = [ x.strip() for x in f.readlines() ]
    diag = DiagnosticReport(readings)
    print(diag.life_support_rating)
