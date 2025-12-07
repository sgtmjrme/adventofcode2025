#!/usr/bin/env python3

def p1(file: str):
    cur_lines = []
    count = 0
    with open(file,'r') as f: 
        line = f.readline().strip()
        start = line.find('S')
        cur_lines = [False] * len(line)
        cur_lines[start] = True
        for line in f:
            for i,c in enumerate(line):
                if c == '^' and cur_lines[i]:
                    if i > 0: cur_lines[i-1] = True
                    cur_lines[i] = False
                    if i < len(line)-1: cur_lines[i+1] = True
                    count += 1
    return count

def p2(file: str):
    lines = []
    with open(file,'r') as f:
        lines = [line.strip() for line in f.readlines()]
    counts = [0] * len(lines[0])
    for line in reversed(lines):
        for i,c in enumerate(line.strip()):
            if c == '^':
                counts[i] = 0 #Cannot propagate through a ^
                if i > 0: counts[i] += counts[i-1] #Add timelines from the left
                if i <= len(line) - 1: counts[i] += counts[i+1] #Add timelines from the right
                counts[i] += 1 #We just made a timeline
            if c == 'S': return counts[i] + 1 #Start of the timeline

if __name__ == '__main__':
    file = 'day7.input'
    print(p1(file))
    print(p2(file))
