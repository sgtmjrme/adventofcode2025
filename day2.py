#!/usr/bin/env python3

def p1(twice: bool = True) -> int:
    out = 0
    with open('day2.input','r') as f:
        line = f.readline().strip()
        for item in line.split(','):
            start,end = (int(x) for x in item.split('-'))
            for i in range(start,end+1): #For each number in the range
                stri = str(i)
                if len(stri) < 2: continue #Do not try with a single number
                if twice and len(stri)/2 % 1 != 0: continue
                for j in (range(len(stri)//2) if not twice else [len(stri)/2-1]): #For each substring length in num
                    numSplits = len(stri)/(j+1)
                    if not numSplits == int(numSplits): continue #Not an integer
                    numSplits = int(numSplits)
                    if twice: j = int(j)
                    substr = stri[0:j+1]
                    if all(x == substr for x in (stri[(j+1)*y:(j+1)*(y+1)] for y in range(numSplits))):
                        print(i)
                        out += i
                        break
    return out

def p2() -> int:
    return p1(False)

def main():
    print(p1())
    print(p2())

if __name__ == '__main__':
    main()
