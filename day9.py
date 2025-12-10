#!/usr/bin/env python3

lines = []
with open('day9.input','r') as f: lines = f.readlines()
#P1 is a 1 liner... although I wish the splits could be better
print(max([abs(int(line.split(',')[0])-int(l.split(',')[0])+1)*abs(int(line.split(',')[1])-int(l.split(',')[1])+1) for line in lines for l in lines]))

from dataclasses import dataclass

@dataclass
class Point():
    x: int
    y: int
    def __init__(self,s: str):
        self.x,self.y = [int(x) for x in s.split(',')]

walls: 'list[tuple[Point,Point]]' = []
for i in range(len(lines)):
    walls.append((Point(lines[i-1]),Point(lines[i])))
    
def box_wall_intersect(box: 'tuple[Point,Point]', wall: 'tuple[Point,Point]') -> bool:
    if max(box[0].x,box[1].x) < min(wall[0].x,wall[1].x) + 1: return False
    if max(box[0].y,box[1].y) < min(wall[0].y,wall[1].y) + 1: return False
    if min(box[0].x,box[1].x) > max(wall[0].x,wall[1].x) - 1: return False
    if min(box[0].y,box[1].y) > max(wall[0].y,wall[1].y) - 1: return False
    return True #They have to intersect at this point
def box_size(box: 'tuple[Point,Point]') -> int:
    return (abs(box[0].x-box[1].x) + 1)*(abs(box[0].y-box[1].y) + 1)

allPoints = [Point(lines[i]) for i in range(len(lines))]
# import pdb
# pdb.set_trace()

maxArea = 0
for i,ipoint in enumerate(allPoints):
    for j,jpoint in enumerate(allPoints):
        if j <= i: continue #Yeah, whatever
        # if ipoint == Point('9,5') and jpoint == Point('2,3'):
            # pdb.set_trace()
        box = (ipoint,jpoint)
        if any(box_wall_intersect(box,wall) for wall in walls): continue
        #We have a valid box - is it bigger?
        maxArea = max(box_size(box),maxArea)
print(maxArea)
