from datetime import datetime
import pickle
from common_function import *
from random import randint

def start_solution_1_b(photos_list):
    start = datetime.now()
    order_slide = solution_1_b(photos_list)
    stop = datetime.now()
    print("Run time: {} for input file {}".format((stop - start), 2))
    return order_slide


def solution_1_b(photos_list):
    start_image = randint(0, len(photos_list)-1)
    while photos_list[start_image].orientation != "V":
        start_image = randint(0, len(photos_list) - 1)
    unhandle_photos = set(range(len(photos_list)))
    curr_index = start_image
    pieces = []
    handled_photos_in_order = []
    count = 0
    while len(unhandle_photos) != 0 and curr_index != -1:
        count += 1
        if count % 500 == 0:
            print("{} - {} - Processing Image Number {}".format(datetime.now(), count, curr_index))

        unhandle_photos.remove(curr_index)
        handled_photos_in_order.append(photos_list[curr_index])

        max_score = -1
        max_index = -1
        for i in unhandle_photos:
            if this_image_must_be_vertical(handled_photos_in_order, photos_list[i]):
                continue
            score = scoring(photos_list[curr_index], photos_list[i])
            if score > max_score:
                max_score = score
                max_index = i

        curr_index = max_index

    for index, p in enumerate(pieces):
        # print("Line: {} - {}".format(index, [str(i) for i in p]))
        print("Line: {} - {}".format(index, [str(i.orientation) for i in p]))

    # Saving to pickle file
    # saveToPickle("pieces_" + str(i) + ".pickle", pieces)
    return handled_photos_in_order


def this_image_must_be_vertical(handled_photo, image):
    count = 0
    for i in reversed(handled_photo):
        if i.orientation == "H":
            break
        count += 1

    if count % 2 == 1:
        return image.orientation != "V"
    else:
        return False


def saveToPickle(fname, var):
    pickle_out = open(fname, "wb")
    pickle.dump(var, pickle_out)
    pickle_out.close()
