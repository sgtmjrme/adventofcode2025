#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    def __hash__(self):
        return int(f'{self.x*1000000000}{self.y}')

def p1():
    map = []
    heightMap = {}
    with open('day4.input','r') as f:
        for line in f:
            map.append(line.strip())
    map_height = len(map)
    map_width = len(map[0])
    remove: 'set[Point]' = set()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '@':
                count = 0
                for j in range(y-1,y+2):
                    if j < 0 or j >= map_height: continue
                    for i in range(x-1,x+2):
                        if i < 0 or i >= map_width: continue
                        if map[j][i] == '@': 
                            heightMap[f'{i},{j}'] = heightMap.get(f'{i},{j}',0) + 1
                            count += 1
                if count < 5: remove.add(Point(x,y))

    print(len(remove))
    return remove,heightMap,map_height,map_width

def printHeightMap(width, height, points):
    for j in range(height):
        for i in range(width):
            print(points.get(f'{i},{j}','.'),end='')
        print()

def p2():
    startlist,map,map_height,map_width = p1()
    count = 0
    while startlist:
        p = startlist.pop()
        count += 1
        del map[f'{p.x},{p.y}']
        for i in range(p.x - 1,p.x + 2):
            if i < 0 or i >= map_width: continue
            for j in range(p.y - 1, p.y + 2):
                if j < 0 or j >= map_height: continue
                if i == p.x and j == p.y: continue
                if f'{i},{j}' not in map: continue
                map[f'{i},{j}'] -= 1
                if map[f'{i},{j}'] < 5: 
                    startlist.add(Point(i,j))
    print(count)

if __name__ == '__main__':
    p2()
