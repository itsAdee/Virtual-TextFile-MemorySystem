class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []
        self.parent = None
        self.level = 1;

    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)
        directory.parent = self
        directory.level = self.level + 1

    def add_file(self, file):
        self.files.append(file)
    
    def isDirectory(self):
        return True

    def isFile(self):
        return False

    def __str__(self) -> str:
        return self.name
