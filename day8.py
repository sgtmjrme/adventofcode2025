#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __init__(self, s:str):
        self.x,self.y,self.z = (int(a) for a in s.split(','))

    def distsqr(self,p2):
        return (p2.x - self.x)**2 + (p2.y - self.y)**2 + (p2.z - self.z)**2
    
    def __str__(self):
        return f'{self.x},{self.y},{self.z}'
    
    def __hash__(self):
        return self.x*1000000000000 + self.y * 1000000 + self.z

# def stringOrder(p1: Point, p2: Point):
    # return (p1,p2}' if p1.x < p2.x else f'{p2},{p1}'

import pdb

def part1(file: str, numConn, dop2: bool = False) -> str:
    groups: 'list[set[Point]]' = []
    distances: 'dict[int,list[tuple[Point,Point]]]' = {}
    points = []
    with open(file,'r') as f:
        for line in f:
            newPoint = Point(line)
            for point in points:
                dist = Point.distsqr(point,newPoint)
                if not dist in distances: distances[dist] = []
                distances[dist].append((point,newPoint))
            points.append(newPoint)
    numPoints = len(points)
    #Now connect the closest numConn
    num = 0
    for key in sorted(distances.keys()):
        if not dop2 and num >= numConn: break
        for connection in distances[key]:
            hit_group = None
            for group in groups:
                if any(conn in group for conn in connection):
                    # print(f'Connecting {connection} to {group}')
                    group.update(connection)
                    hit_group = group
                    break
            else:
                # print(f'No group found - adding new group')
                groups.append(set(connection))
            #Combine groups?  Each connection can only possibly bind 2
            if hit_group: 
                actually_touch = False
                for group in groups:
                    if group == hit_group: continue
                    if len(group.intersection(hit_group)) > 0:
                        group.update(hit_group)
                        actually_touch = True
                        break
                if actually_touch: groups.remove(hit_group)
            num += 1
            if len(groups) == 1 and len(groups[0]) == numPoints: 
                #We have our last connection?
                print(f'Total connections was {num}')
                return connection[0].x * connection[1].x
    #p1
    if not dop2: 
        top3 = sorted(groups,key=lambda x: len(x))[-3:]
        out = 1
        for i in top3: out *= len(i)
    return out

if __name__ == '__main__':
    file = 'day8.input'
    # print(part1(file,10 if 'sample' in file else 1000)) #131150
    print(part1(file,None,True))
