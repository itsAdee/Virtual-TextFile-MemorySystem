class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []

    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)

    def add_file(self, file):
        self.files.append(file)
