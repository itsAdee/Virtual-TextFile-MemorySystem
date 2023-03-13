import random


class File:
    ids = set()

    def __init__(self, name):
        self.name = name
        self.pointer = 0
        self.file_size = 0
        self.blocks = list()
        self.id = random.randint(0, 1000000)
        while self.id in File.ids:
            self.id += 1
        File.ids.add(self.id)

    def write(self, data, MainMemory):
        size = len(data)
        freed_blocks = self.blocks.copy()
        self.blocks.clear()
        MainMemory.free_blocks(freed_blocks)
        self.file_size = size
        blockes_needed = size // 64
        self.pointer = 0
        for i in range(blockes_needed + 1):
            block = MainMemory.allocate_block(self.id)
            MainMemory.blocks[block] = data[self.pointer:self.pointer + 64]
            self.blocks.append(block)
            if size < 64:
                self.pointer += size
                size = 0
            else:
                self.pointer += 64
                size -= 64

    def append(self, data, MainMemory):
        size = len(data)
        current_pointer = 0
        self.file_size += size
        last_block = self.blocks[-1]
        if MainMemory.space_left_in_a_block(last_block) >= 0:
            MainMemory.blocks[last_block] += data[0:
                                                  MainMemory.space_left_in_a_block(last_block)]
            current_pointer += MainMemory.space_left_in_a_block(last_block)
        blockes_needed = (size - current_pointer) // 64
        for i in range(blockes_needed + 1):
            block = MainMemory.allocate_block(self)
            self.blocks.append(block)
            MainMemory.blocks[block] = data[current_pointer:current_pointer + 64]
            if size < 64:
                current_pointer += size
                size = 0
            else:
                current_pointer += 64
                size -= 64
        self.pointer += current_pointer

    def isDirectory(self):
        return False

    def isFile(self):
        return True

    def __str__(self):
        return self.name + " " + str(self.id)
