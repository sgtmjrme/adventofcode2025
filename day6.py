#!/usr/bin/env python3

def p1(file: str):
    operators = []
    nums = []
    with open(file,'r') as f:
        operators = f.readline().strip().split()
        nums = [int(x) for x in f.readline().strip().split()]
        for line in f:
            splits = line.strip().split()
            for i,val in enumerate(splits):
                if operators[i] == '+':
                    nums[i] += int(val)
                if operators[i] == '*':
                    nums[i] *= int(val)
    return sum(nums)    

def do_calc(operators: 'list[str]', nums: 'list[str]'):
    total = 0
    if operators.pop() == '+':
        total += sum(int(x) for x in nums)
    else:
        tmp = int(nums.pop())
        for num in nums:
            tmp *= int(num)
        total += tmp
    return total


def p2(file: str):
    operators = []
    nums = []
    with open(file,'r') as f:
        operators = f.readline().strip().split()
        nums = [a for a in f.readline()]
        for line in f:
            splits = [a for a in line]
            for i,val in enumerate(splits):
                nums[i] += val
    nums.pop() #Remove trailing newlines
    to_combine = []
    total = 0
    while len(nums):
        val = nums.pop()
        if val.strip() == '':
            total += do_calc(operators, to_combine)
            to_combine.clear()
        else:
            to_combine.append(val)
    total += do_calc(operators, to_combine)
    return total

if __name__ == '__main__':
    f = 'day6.input'
    print(p1(f))
    print(p2(f))
