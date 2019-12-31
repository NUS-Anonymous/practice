from datetime import datetime
from common_function import *


def start_solution_4(photos_list):
    start = datetime.now()
    pieces = solution_4(photos_list)
    stop = datetime.now()
    print("Run time: {} for input file {}".format((stop - start), 2))


def solution_4(photos_list):
    score_board = [{} for i in range(len(photos_list))]
    key_string = "{}-{}->{}-{}"
    for r in range(len(photos_list)):
        for c in range(r + 1, len(photos_list)):
            if photos_list[r].orientation == "V" and photos_list[c].orientation== "V":
                continue
            score = scoring(photos_list[r], photos_list[c])
            if score != 0:
                score_board[r][key_string.format(r, photos_list[r].orientation, c, photos_list[c].orientation)] = score

    # Merge All list
    resulted_list = {}
    for r in range(len(photos_list)):
        resulted_list.update(score_board[r])

    sorted_list = sorted(resulted_list.items(), key=lambda sb: (sb[1], sb[0]))
    sorted_list.reverse()

    # At this point you have a list of all the values

    return sorted_list
