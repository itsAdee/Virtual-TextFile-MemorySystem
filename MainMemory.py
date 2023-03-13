class MainMemory:
    def __init__(self):
        self.block_size = 64
        self.blocks = [None] * 1024

    def allocate_block(self, id):
        for i in range(len(self.blocks)):
            if self.blocks[i] is None:
                self.blocks[i] = id
                return i

    def free_blocks(self, freed_blocks):
        for i in range(len(self.blocks)):
            if i in freed_blocks:
                self.blocks[i] = None

    def print_blocks(self):
        for i in range(len(self.blocks)):
            if self.blocks[i] is not None:
                print(i, self.blocks[i])

    def space_left_in_a_block(self, block):
        return self.block_size - len(self.blocks[block])
