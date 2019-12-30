class Image:
    def __init__(self, orientation, numb_of_tags, tags):
        self.orientation = orientation
        self.numb_of_tags = numb_of_tags
        self.tags = tags

    def __str__(self):
        return str([self.orientation, self.numb_of_tags, self.tags])