#!/usr/bin/env python3

from functools import lru_cache

def read_input(file: str) -> 'dict[str,list[str]]':
    out: 'dict[str,list[str]]' = {}
    with open(file,'r') as f:
        for line in f:
            splits = line.strip().split()
            out[splits[0][:-1]] = splits[1:]
    return out

@lru_cache(maxsize=10000)
def dfs(start: str, end: str, hit_fft: bool = False, hit_dac: bool = False, p2: bool = False) -> int:
    #WARNING - DOES NOT CHECK FOR LOOPS
    global input_map
    hit_dac = hit_dac or start == 'dac'
    hit_fft = hit_fft or start == 'fft'
    if start == end: 
        return hit_dac and hit_fft if p2 else 1
    cnt: int = 0
    for s in input_map[start]:
        cnt += dfs(s,end,hit_fft,hit_dac,p2)
    return cnt

if __name__ == '__main__':
    file = 'day11.input'
    global input_map
    input_map = read_input(file)
    print(f'P1: {dfs('you','out')}')
    print(f'P2: {dfs('svr','out',p2 = True)}')
