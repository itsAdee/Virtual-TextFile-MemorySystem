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
    file_system.MemoryMap()

else:
    create_file_system()
