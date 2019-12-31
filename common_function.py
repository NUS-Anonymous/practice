from image import Image

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
    return photos_list

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


def scoring(image1, image2):
    common_tags = image1.tags & image2.tags
    return min(image1.numb_of_tags - len(common_tags), image2.numb_of_tags - len(common_tags), len(common_tags))
