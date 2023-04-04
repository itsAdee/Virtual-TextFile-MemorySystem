from FileManagementSystem import *

file_system = FileManagementSystem()


def create_file_system():
    print("Creating new file system...\n")
    file_system.create_file("fileInRoot.txt")
    file_system.create_directory("dir1")
    file_system.create_file("fileInDir1.txt")
    
    file_system.write_file("fileInDir1.txt", "Hello World\n")
    file_system.append_file("fileInDir1.txt", "Hello From the other side")
    print(file_system.readFile("fileInDir1.txt"))

    # file_system.save()
    file_system.MemoryMap()


if os.path.exists("file_system.pickle"):
    print("Loading file system...\n")
    file_system = file_system.load()


else:
    create_file_system()

######################### File System #########################


# print("Creating new files...\n")
# file_system.create_file("testfile1.txt")

# myfile = file_system.write_file(
#     "testfile1.txt", "Hello World ")
# memory = file_system.Memory

# memory.print_blocks()

# file_system.MoveContent("testfile1.txt", 6, 8, 1)

# # print(myfile)
# # print(myfile.blocks)
# # print(myfile.file_size)

# # file_system.append_file("testfile1.txt", "they also call me mbaku")
# # file_system.append_file(
# #     "testfile1.txt", "but you can also address me as the king of the jungle")
# # file_system.write_file("testfile1.txt", "Hello World bajoka ")

# print(myfile.blocks)
# print(myfile.file_size)

# memory.print_blocks()
