#scoring_matrix
# column: what i play (X,Y,Z)
# row: what the competitor plays (A,B,C)
import numpy as np

scoring_matrix = np.array([[3, 6, 0], [0, 3, 6], [6, 0, 3]])
def SolutionPart1(strategy_tuple, scoring_matrix):
    """strategy_tuple: (competitor, i)"""
    mapping = {"A":0,"B":1,"C":2, "X":0, "Y":1, "Z":2}
    translated_strategy = (mapping[strategy_tuple[0]], mapping[strategy_tuple[1]])
    game_result = scoring_matrix[translated_strategy[0]][translated_strategy[1]]
    my_play_score = translated_strategy[1] + 1
    return game_result + my_play_score
#print(SolutionPart1(("C","Z"), scoring_matrix))

with open("./inputs/Day2Part1.txt")as f:
    inputs = [tuple([x for x in line.split()]) for line in f]
    print("Answer: ",sum([SolutionPart1(i, scoring_matrix) for i in inputs]))


def SolutionPart2(strategy_tuple, scoring_matrix):
    """strategy_tuple: (competitor, i)"""
    component_index_mapping = {"A": 0, "B": 1, "C": 2}
    iplay_mapping = {"X": 0, "Y": 3, "Z": 6}
    reversed_iplay = {0:"X",1:"Y",2:"Z"}
    competitor_play = component_index_mapping[strategy_tuple[0]]
    score_desired = iplay_mapping[strategy_tuple[1]]
    whatishouldplay = reversed_iplay[np.where(scoring_matrix[competitor_play] == score_desired)[0][0]]
    return whatishouldplay

with open("./inputs/Day2Part1.txt")as f:
    inputs = [tuple([x for x in line.split()]) for line in f]
    print("Answer: ",sum([SolutionPart1(tuple([i[0],SolutionPart2(i, scoring_matrix)]), scoring_matrix) for i in inputs]))
