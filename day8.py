#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __init__(self, s:str): #Tobuild a point, give a comma delimited string
        self.x,self.y,self.z = (int(a) for a in s.split(','))

    def distsqr(self,p2): #Simple distance (squared only)
        return (p2.x - self.x)**2 + (p2.y - self.y)**2 + (p2.z - self.z)**2
    
    def __str__(self): #For printing (and for debugging)
        return f'{self.x},{self.y},{self.z}'
    
    def __hash__(self): #Because sets need a hash, and frick you
        return self.x*1000000000000 + self.y * 1000000 + self.z

def part1(file: str, numConn, dop2: bool = False) -> str:
    distances: 'dict[int,list[tuple[Point,Point]]]' = {} #Keep a list of all points that give a given distance
    points = []
    with open(file,'r') as f:
        for line in f:
            newPoint = Point(line)
            for point in points: #Find the distance from this point to all other points I know about
                dist = Point.distsqr(point,newPoint)
                if not dist in distances: distances[dist] = []
                distances[dist].append((point,newPoint)) #Add the new distance to my hash
            points.append(newPoint)
    numPoints = len(points) #Used for P2 for exit condition
    #Now connect the closest numConn
    num = 0
    groups: 'list[set[Point]]' = [] # Hold all groups I know about
    for key in sorted(distances.keys()): #For each distance, lowest to highest
        if not dop2 and num >= numConn: break #If doing p1, exit after numConn connections have been made
        for connection in distances[key]: #For each connection at that distance
            hit_group = None
            for group in groups: #For all groups I currently know about
                if group.intersection(connection): # If any point from that connection is already in a group, add the connection to that group
                    group.update(connection)
                    hit_group = group #But also keep track of what group I hit
                    break
            else: #I didn't find any group with either point in it - it's a new group now
                groups.append(set(connection))
            num += 1 #Number of connections added
            # We connected the connection to one group... but it has 2 points, so it may hit another group
            # So check whether the group we just hit now hits any other group
            if hit_group: 
                actually_touch = False #Keep track if we actually hit a group
                for group in groups:
                    if group == hit_group: continue #Don't hit our own group!
                    if len(group.intersection(hit_group)) > 0: #We hit another group - add our current group to it
                        group.update(hit_group)
                        actually_touch = True #And keep track that we did
                        break
                
                if actually_touch: groups.remove(hit_group) #If we had hit a group, remove the "old" one
            if len(groups) == 1 and len(groups[0]) == numPoints: #If we have 1 group, and it contains all points, we're done for P2
                #We have our last connection?
                print(f'Total connections was {num}')
                return connection[0].x * connection[1].x #Thankfully, the way I coded this I had easy access to that last connection
    #p1
    if not dop2: 
        top3 = sorted(groups,key=lambda x: len(x))[-3:] #Sort the groups by the # of points they have in them
        out = 1
        for i in top3: out *= len(i) #And just return the multiplication
    return out

if __name__ == '__main__':
    file = 'day8.input'
    # print(part1(file,10 if 'sample' in file else 1000)) #131150
    print(part1(file,None,True))
