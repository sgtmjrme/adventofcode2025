#!/usr/bin/env python3

from dataclasses import dataclass
    
@dataclass
class FreshRange():
    start: int
    end: int
    def __init__(self,val):
        self.start = val[0]
        self.end = val[1]

def encompasses(range1: FreshRange, range2: FreshRange):
    if range1.start <= range2.start and range1.end >= range2.end:
        return True

def inside(range1: FreshRange, range2: FreshRange):
    for i in [range1.start, range1.end]:
        if i >= range2.start and i <= range2.end: return True
    return False

if __name__ == '__main__':
    ranges: list[FreshRange] = []
    intlines = []
    with open('day5.input','r') as f:
        #read fresh ranges
        while line := f.readline():
            if line.strip() == '': break
            ranges.append(FreshRange([int(x) for x in line.split('-')]))
        for line in f:
            intlines.append(int(line))
    final_ranges: list[FreshRange] = []
    for i in range(len(ranges)):
        test_range = ranges[i]
        for j in range(i+1,len(ranges)):
            if encompasses(ranges[j],test_range): break
            if inside(test_range,ranges[j]) or inside(ranges[j],test_range):
                ranges[j].start = min(test_range.start,ranges[j].start)
                ranges[j].end = max(test_range.end,ranges[j].end)
                break
        else:
            final_ranges.append(test_range)
    print(final_ranges)
            
    count = 0
    for intline in intlines:
        for r in final_ranges:
            if intline >= r.start and intline <= r.end: count += 1
    print(count)

    #P2
    p2 = 0
    for r in final_ranges:
        p2 += r.end - r.start + 1
    print(p2)
