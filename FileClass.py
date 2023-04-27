import random


class File:
    ids = set()

    def __init__(self, name):
        self.name = name
        self.pointer = 0
        self.file_size = 0
        self.blocks = list()
        self.isBeingRead = False
        self.isBeingWritten = False
        self.id = random.randint(1, 1000000)
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
        new_data = data[:size]
        self.write(new_data, MainMemory)

    def read(self, MainMemory):
        data = ""
        for block in self.blocks:
            data += MainMemory.blocks[block]
        return data
    
    def open(self, mode, log):
        if mode == "r":
            if self.isBeingWritten:
                log.write(f"File {self.name} read failed: File is being written to")
                return False
            self.isBeingRead = True
            return True
        elif mode == "w":
            if self.isBeingRead:
                log.write(f"File {self.name} write failed: File is being read")
                return False
            self.isBeingWritten = True
            return True
        
    def close(self, log):
        if self.isBeingRead:
            self.isBeingRead = False
        elif self.isBeingWritten:
            self.isBeingWritten = False
        else:
            log.write(f"File {self.name} close failed: File is not open")

    def isDirectory(self):
        return False

    def isFile(self):
        return True

    def __str__(self):
        return self.name + " " + str(self.id)
