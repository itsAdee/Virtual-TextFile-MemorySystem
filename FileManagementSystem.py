import os
import pickle
from FileClass import File
from DirectoryClass import Directory
from MainMemory import MainMemory


class FileManagementSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root
        self.files = {}
        self.Memory = MainMemory()
        self.subdirectories = {}

    def create_file(self, name):
        file = File(name)
        self.files[name] = file
        self.current_directory.add_file(file)

    def create_directory(self, name):
        directory = Directory(name)
        self.subdirectories[name] = directory
        self.current_directory.add_subdirectory(directory)
        # self.change_directory(name)

    def delete_file(self, name):
        current_directory = self.current_directory
        for file in current_directory.files:
            if file.name == name:
                current_directory.remove_file(file)
                self.files.pop(name)
                return

    def append_file(self, name, data):
        try:
            file = self.files[name]
            file.append(data, self.Memory)
        except:
            print("The current directory has no such file")

    def write_file(self, name, data):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            my_file.write(data, self.Memory)
            return my_file
        except:
            print("The current directory has no such file")

    def truncate_file(self, name, size):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            my_file.truncatefile(self.Memory, size)
        except:
            print("The current directory has no such file")

    def readFile(self, name):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            return my_file.read(self.Memory)
        except:
            print("The current directory has no such file")

    def MoveContent(self, name, start, end, newstart):
        current_directory = self.current_directory
        my_file = current_directory.find_file(name)
        my_file.moveContentWithinFile(self.Memory, start, end, newstart)

    def change_directory(self, name):
        if self.current_directory.parent == None and name == "..":
            return

        if name == "..":
            self.current_directory = self.current_directory.parent
        elif name == "root":
            self.current_directory = self.root
        else:
            for directory in self.current_directory.subdirectories:
                if directory.name == name:
                    self.current_directory = directory
                    return

    def moveFileInDirectory(self, fileName, newDirectory):
        current_directory = self.current_directory
        my_file = current_directory.find_file(fileName)
        current_directory.remove_file(my_file)
        
        if newDirectory == "..":
            if current_directory.parent == None:
                return
            
            current_directory = current_directory.parent
            current_directory.add_file(my_file)
            return

        newFileDirectory = newDirectory.split("/")
        for i in newFileDirectory:
            if i == "":
                continue
            for directory in current_directory.subdirectories:
                if directory.name == i:
                    current_directory = directory
                    break
            
        current_directory.add_file(my_file)

    def passWorkingDirectory(self):
        current_directory = self.current_directory
        path = ""
        while current_directory != None and current_directory.parent is not None:
            path = "/" + current_directory.name + path
            current_directory = current_directory.parent
        if path == "":
            path = "/"
        return path

    def MemoryMap(self, current_directory=None):
        if current_directory is None:
            current_directory = self.root
            print("/")

        spaces = current_directory.level * 2
        for file in current_directory.files:
            blocks = ""
            for block in file.blocks:
                blocks += str(block) + ","
            print(" " * spaces + file.name + " " + str(file.id) +
                  " " + str(file.file_size) + " " + blocks)
        for directory in current_directory.subdirectories:
            if directory.name == self.current_directory.name:
                print(" " * spaces + "*" + directory.name + "/")
            else:
                print(" " * spaces + directory.name + "/")
            self.MemoryMap(directory)

    def save(self):
        with open("file_system.pickle", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        with open("file_system.pickle", "rb") as file:
            return pickle.load(file)

    def listAll(self):
        for i in self.current_directory.subdirectories:
            print(i)
        for i in self.current_directory.files:
            print(i)

    '''
    Adding the Terminal Interface
    '''

    def terminal(self):
        while True:
            prompt = input("\n> ").split(" ")
            command = prompt[0]

            # Exit the terminal
            if command == "exit":
                break
            
            # Print the help menu
            elif command == "help":
                print(
                    """Commands:
                ls - list all files and directories
                pwd - print working directory
                cd - change directory
                mkdir - make directory
                touch - create file
                rm - remove file
                wr - write to file
                ap - append to file
                tr - truncate file
                mvc - move content within file
                mvf - move file to another directory
                cat - read file
                mmap - show memory map
                help - show list of commands
                save - save file system
                exit - exit terminal
                """)
                pass
            
            # List all files and directories in the current directory
            elif command == "ls":
                self.listAll()
                pass
            
            # Pass the working directory
            elif command == "pwd":
                print(self.passWorkingDirectory())
            
            # Change Directory
            elif command == "cd":
                self.change_directory(prompt[1])
                pass
            
            # Create a directory
            elif command == "mkdir":
                self.create_directory(prompt[1])
                pass
            
            # Create a file
            elif command == "touch":
                self.create_file(prompt[1])
                pass
            
            # Read a file
            elif command == "rm":
                self.delete_file(prompt[1])
                pass
            
            # Write to a file
            elif command == "wr":
                written_text = ""
                for i in range(2, len(prompt)):
                    written_text += prompt[i] + " "
                self.write_file(prompt[1], written_text)
            
            # Append to a file
            elif command == "ap":
                appended_text = ""
                for i in range(2, len(prompt)):
                    appended_text += prompt[i] + " "
                self.append_file(prompt[1], appended_text)
            
            # Truncate a file
            elif command == "tr":
                self.truncate_file(prompt[1], prompt[2])
            
            # Move content within a file
            elif command == "mvc":
                self.MoveContent(prompt[1], int(
                    prompt[2]), int(prompt[3]), int(prompt[4]))
            
            # Move a file to a different directory
            elif command == "mvf":
                self.moveFileInDirectory(prompt[1], prompt[2])

            # Read a file
            elif command == "cat":
                print("the file is: ", prompt[1])
                print(self.readFile(prompt[1]))
                pass
            
            # Show the memory map
            elif command == "mmap":
                self.MemoryMap()
                pass
            
            # Save the file system
            elif command == "save":
                self.save()
            
            # Invalid command
            else:
                print("Invalid Command")
                print("Type 'help' for a list of commands")
