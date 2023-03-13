import random


class File:
    ids = set()

    def __init__(self, name):
        self.name = name
        self.pointer = 0
        self.blocks = []
        self.id = random.randint(0, 1000000)
        while self.id in File.ids:
            self.id += 1
        File.ids.add(self.id)

    def write(self, data, MainMemory):
        size = len(data)
        blockes_needed = size // 64
        self.pointer = 0
        for i in range(blockes_needed):
            block = MainMemory.allocate_block(self)
            MainMemory.blocks[block] = data[self.pointer:self.pointer + 64]
            self.blocks.append(block)
            self.pointer += 64

    def append(self, data, MainMemory):
        size = len(data)
        blockes_needed = size // 64
        for i in range(blockes_needed + 1):
            block = MainMemory.allocate_block(self)
            self.blocks.append(block)
            MainMemory.blocks[block] = data[self.pointer:self.pointer + 64]
            self.pointer += 64

    def isDirectory(self):
        return False
    
    def isFile(self):
        return True

    def __str__(self):
        return self.name + " " + str(self.id)
