import numpy as np
def SolutionPart1(input_data):
    with open(input_data) as f:
        input = f.read()

    input = [int(i) if i!="" else 0 for i in input.split("\n")]
    # find sepearations:
    sep_indexs = [-1] + [i for (i,x) in enumerate(input) if x==0]
    return (max([sum(input[sep_indexs[i-1]+1: sep_indexs[i]]) for i in range(len(sep_indexs)) if i>=1]))

print(SolutionPart1("./inputs/Day1Part1.txt"))

def SolutionPart2(input_data):
    with open(input_data) as f:
        input = f.read()

    input = [int(i) if i!="" else 0 for i in input.split("\n")]
    # find sepearations:
    sep_indexs = [-1] + [i for (i,x) in enumerate(input) if x==0]
    return sum(sorted([sum(input[sep_indexs[i-1]+1: sep_indexs[i]]) for i in range(len(sep_indexs)) if i>=1], reverse=True)[:3])

print(SolutionPart2("./inputs/Day1Part1.txt"))