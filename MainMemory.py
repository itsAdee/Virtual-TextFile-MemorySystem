class MainMemory:
    def __init__(self):
        self.block_size = 64
        self.blocks = [None] * 1024

    def allocate_block(self, file):
        for i in range(len(self.blocks)):
            if self.blocks[i] is None:
                self.blocks[i] = file
                return i

    def free_blocks(self, file):
        for i in range(len(self.blocks)):
            if self.blocks[i] == file:
                self.blocks[i] = None
