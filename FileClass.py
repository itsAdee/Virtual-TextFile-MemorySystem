import random


class File:
    ids = set()

    def __init__(self, name):
        self.name = name
        self.pointer = 0
        self.file_size = 0
        self.blocks = list()
        self.id = random.randint(1, 1000000)
        while self.id in File.ids:
            self.id += 1
        File.ids.add(self.id)

    def write(self, data, MainMemory):
        size = len(data)
        freed_blocks = self.blocks.copy()
        self.file_size = size
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
            space_left = MainMemory.space_left_in_a_block(last_block)
            MainMemory.blocks[last_block] += data[0:
                                                  space_left]
            current_pointer += space_left
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

    def moveContentWithinFile(self, MainMemory, start, size, new_start):
        my_blocks = self.blocks.copy()
        data = ""
        for block in my_blocks:
            data += MainMemory.blocks[block]
        previous_data = data[:start]
        selected_data = data[start:start+size]
        next_data = data[start+size:]
        new_data = previous_data[:new_start] + \
            selected_data + previous_data[new_start:] + next_data
        pointer = 0
        for block in my_blocks:
            MainMemory.blocks[block] = new_data[pointer:pointer + 64]
            pointer += 64
            if pointer > len(new_data):
                break

    def truncatefile(self, MainMemory, size):
        self.file_size = size
        my_blocks = self.blocks.copy()
        data = ""
        for block in my_blocks:
            data += MainMemory.blocks[block]
        free_blocks = my_blocks
        self.blocks.clear()
        MainMemory.free_blocks(free_blocks)
        new_data = data[:size]
        self.write(new_data, MainMemory)

    def delete(self, MainMemory):
        self.file_size = 0
        my_blocks = self.blocks.copy()
        self.blocks.clear()
        MainMemory.free_blocks(my_blocks)

    def read(self, MainMemory):
        data = ""
        for block in self.blocks:
            data += MainMemory.blocks[block]
        return data

    def isDirectory(self):
        return False

    def isFile(self):
        return True

    def __str__(self):
        return self.name + " " + str(self.id)
