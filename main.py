from image import Image
from datetime import datetime
import pickle


def read_file(index):
    directory = "qualification_round_2019.in/"
    fileName = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt"
        , "e_shiny_selfies.txt"]
    filepath = directory + fileName[index];
    photos_list = []
    with open(filepath) as fp:
        # Read First line
        numb_of_images = int(fp.readline())
        print("Processing number of images {}".format(numb_of_images))
        for i in range(numb_of_images):
            inputs = fp.readline().strip().split(" ")
            orientation = inputs[0]
            # numb_of_tags = inputs[1]
            tags = set(inputs[2:])
            photos_list.append(Image(orientation, len(tags), tags))
    return numb_of_images, photos_list


def scoring(image1, image2):
    common_tags = image1.tags & image2.tags
    return min(image1.numb_of_tags - len(common_tags), image2.numb_of_tags - len(common_tags), len(common_tags))


# def create_score_matrix(numb_of_images, photos_list):
#     score_table = {}
#
#     print(score_table)
#     for r in range(numb_of_images):
#         for c in range(r + 1, numb_of_images):
#             # print("Comparing image {} - {}".format(r, c))
#             score = scoring(photos_list[r], photos_list[c])
#             # score_table[r][c] = score
#             # score_table[c][r] = score
#             score_table.put(r, (c, score))
#             score_table.put(c, (r, score))
#     return score_table


def main():
    print("This is Main")
    for i in range(5):
        numb_of_images, photos_list = read_file(i)
        start = datetime.now()
        pieces = solution_1(photos_list)
        # solution_1(photos_list)
        stop = datetime.now()
        print("Run time: {} for input file {}".format((stop - start), i))
        pickle_out = open("pieces_" + str(i) + ".pickle", "wb")
        pickle.dump(pieces, pickle_out)
        pickle_out.close()

    # final_scoring_system(handled_photos_in_order)


def solution_2(photos_list):
    start_image = 0
    unhandle_photos = set(range(len(photos_list)))
    curr_index = start_image
    pieces = []
    handled_photos_in_order = []
    count = 0;
    while len(unhandle_photos) != 0:
        count += 1
        if count % 500 == 0:
            print("{} - {} - Processing Image Number {}".format(datetime.now(), count, curr_index))

        unhandle_photos.remove(curr_index)

        if photos_list[curr_index].orientation == "V":
            handled_photos_in_order.append(photos_list[curr_index])
            pieces.append(handled_photos_in_order)
            handled_photos_in_order = []
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

    return pieces


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

    return pieces


#  Sugar solution
def combine_vertical_images(stack):
    combined_slide = []
    if len(stack) % 2 == 0:
        while len(stack) > 0:
            image1 = stack.pop()
            image2 = stack.pop()
            combine_tags = image1.tags | image2.tags
            combined_image = Image('H', len(combine_tags), combine_tags)
            combined_slide.append(combined_image)
    else:
        print("Error")
    combined_slide.reverse()
    return combined_slide


def final_scoring_system(photos_list):
    final_score = 0
    count = len(photos_list)
    i = 0
    stack = []
    slides = []
    while i < count:
        if photos_list[i].orientation == "V":
            stack.append(photos_list[i])
            if len(stack) == 2:
                combined_slide = combine_vertical_images(stack)
                slides += combined_slide
                stack = []

        if photos_list[i].orientation == "H":
            slides.append(photos_list[i])

        i += 1

    if len(stack) % 2 != 0:
        print("Error")
        return

    print('--------------------------')
    print("Resulted Score Table")
    [print(i) for i in slides]

    for i in range(len(slides) - 1):
        final_score += scoring(slides[i], slides[i + 1])

    print("Final score: " + str(final_score))
    return final_score


if __name__ == "__main__":
    main()
