class File:
    def __init__(self, name, compile_time, replicate_time, dependency):
        self.name = name
        self.compile_time = compile_time
        self.replicate_time = replicate_time
        self.dependency = dependency

    def __str__(self):
        return str([self.name, self.compile_time, self.replicate_time, self.dependency])
