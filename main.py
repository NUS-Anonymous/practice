from solution_2 import *
from solution_4 import *
from solution_1 import *
from common_function import *


def main():
    print("This is Main")
    final_score = []
    for i in range(5):
        photos_list = read_file(i)
        order_slide = start_solution_1(photos_list)
        final_score.append(final_scoring_system(order_slide))
        print("-----------------------------------")
        print()

    print("Final Individual Score")
    print(final_score)


if __name__ == "__main__":
    main()
