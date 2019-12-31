from datetime import datetime
import pickle
from common_function import *


def start_solution_2(photos_list):
    start = datetime.now()
    pieces = solution_2(photos_list)
    processing_pieces(pieces)
    stop = datetime.now()
    print("Run time: {} for input file {}".format((stop - start), 2))


def processing_pieces(pieces):
    new_pieces_combi = []
    for r in range(len(pieces)):
        for c in range(r, len(pieces)):
            comb1, comb2 = scoring_2_pieces(pieces[r], pieces[c])
            new_pieces_combi.append(comb1)
            new_pieces_combi.append(comb2)
    return new_pieces_combi


def scoring_2_pieces(piece1, piece2):
    if len(piece1) == 1 and len(piece2) == 1:
        return piece1, piece2
    if len(piece1) == 1 or len(piece2) == 1:
        combi1 = piece1 + piece2
        combi2 = piece2 + piece1
    else:
        piece2.reverse()
        combi1 = piece2 + piece1
        combi2 = piece1 + piece2

    return (combi1, combi2)


def solution_2(photos_list):
    start_image = 0
    unhandle_photos = set(range(len(photos_list)))
    curr_index = start_image
    pieces = []
    handled_photos_in_order = []
    count = 0
    while len(unhandle_photos) != 0:
        count += 1
        if count % 500 == 0:
            print("{} - {} - Processing Image Number {}".format(datetime.now(), count, curr_index))

        unhandle_photos.remove(curr_index)

        if photos_list[curr_index].orientation == "V":
            handled_photos_in_order.append(photos_list[curr_index])
            pieces.append(handled_photos_in_order)
            handled_photos_in_order = []
            for e in unhandle_photos:
                break
            curr_index = e
            continue
        else:
            handled_photos_in_order.append(photos_list[curr_index])

        max_score = -1
        max_index = -1
        for i in unhandle_photos:
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
    return pieces


def saveToPickle(fname, var):
    pickle_out = open(fname, "wb")
    pickle.dump(var, pickle_out)
    pickle_out.close()


def solution_1(photos_list):
    # Pick 0 as starting:
    start_image = 0
    unhandle_photos = set(range(len(photos_list)))
    curr_index = start_image
    pieces = []
    handled_photos_in_order = []
    count = 0
    while len(unhandle_photos) != 0:
        count += 1

        if count % 500 == 0:
            print("{} - {} - Processing Image Number {}".format(datetime.now(), count, curr_index))

        unhandle_photos.remove(curr_index)

        if photos_list[curr_index].orientation == "V":
            handled_photos_in_order.append(photos_list[curr_index])
            pieces.append(handled_photos_in_order)
            handled_photos_in_order = []
        else:
            handled_photos_in_order.append(photos_list[curr_index])

        max_score = -1
        max_index = -1
        for i in unhandle_photos:
            score = scoring(photos_list[curr_index], photos_list[i])
            if score > max_score:
                max_score = score
                max_index = i

        curr_index = max_index

    for index, p in enumerate(pieces):
        # print("Line: {} - {}".format(index, [str(i) for i in p]))
        print("Line: {} - {}".format(index, [str(i.orientation) for i in p]))

    # Saving to Pickle File
    # pickle_out = open("pieces_" + str(i) + ".pickle", "wb")
    # pickle.dump(pieces, pickle_out)
    # pickle_out.close()
    return pieces
