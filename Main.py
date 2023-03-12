from FileManagementSystem import *

file_system = FileManagementSystem()
if os.path.exists("file_system.pickle"):
    file_system = file_system.load()
    file_system.MemoryMap()
else:
    # file_system.create_directory("home")
    # file_system.create_file("file1")
    # file_system.append_file(
    #     "file1", "Hello World!MynamesisAhmeddwfewfffrerferferfrfrc3f334f43ff34f34f43fS")
    file_system.MemoryMap()
