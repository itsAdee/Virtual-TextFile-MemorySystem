from FileManagementSystem import *

file_system = FileManagementSystem()


def create_file_system():
    print("Creating new file system...\n")
    file_system.create_file("fileInRoot.txt")
    file_system.create_directory("dir1")
    file_system.create_file("fileInDir1.txt")
    file_system.create_directory("dir2")
    file_system.create_file("fileInDir2.txt")

    file_system.append_file("fileInDir1.txt", "Hello World")

    file_system.save()
    file_system.MemoryMap()


if os.path.exists("file_system.pickle"):
    print("Loading file system...\n")
    file_system = file_system.load()


else:
    create_file_system()

######################### File System #########################


print("Creating new files...\n")
file_system.create_file("testfile1.txt")

myfile = file_system.write_file(
    "testfile1.txt", "Hello World My name is John fwfqdqfd They also call me ricardo son of lord zillla")
memory = file_system.Memory

memory.print_blocks()

print(myfile)
print(myfile.blocks)
print(myfile.file_size)

file_system.append_file("testfile1.txt", "they also call me mbaku")
file_system.append_file(
    "testfile1.txt", "but you can also address me as the king of the jungle")

file_system.write_file("testfile1.txt", "Hello World again!")


print(myfile.blocks)
print(myfile.file_size)

memory.print_blocks()
