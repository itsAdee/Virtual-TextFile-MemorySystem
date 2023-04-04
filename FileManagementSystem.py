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
        file = self.files[name]
        file.append(data, self.Memory)

    def write_file(self, name, data):
        current_directory = self.current_directory
        my_file = current_directory.find_file(name)
        my_file.write(data, self.Memory)
        return my_file

    def truncate_file(self, name, size):
        current_directory = self.current_directory
        my_file = current_directory.find_file(name)
        my_file.truncatefile(self.Memory, size)

    def readFile(self, name):
        current_directory = self.current_directory
        my_file = current_directory.find_file(name)
        return my_file.read(self.Memory)

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
            print(" " * spaces + file.name + " " + str(file.id))
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

            if command == "exit":
                break
            elif command == "help":
                print(
                """Commands:
                ls - list all files and directories
                pwd - print working directory
                cd - change directory
                mkdir - make directory
                touch - create file
                rm - remove file
                cat - read file
                mmap - show memory map
                help - show list of commands
                exit - exit terminal
                """)
                pass
            elif command == "ls":
                self.listAll()
                pass
            elif command == "pwd":
                print(self.passWorkingDirectory())
            elif command == "cd":
                self.change_directory(prompt[1])
                pass
            elif command == "mkdir":
                self.create_directory(prompt[1])
                pass
            elif command == "touch":
                self.create_file(prompt[1])
                pass
            elif command == "rm":
                self.delete_file(prompt[1])
                pass
            elif command == "cat":
                self.readFile(prompt[1])
                pass
            elif command == "mmap":
                self.MemoryMap()
                pass
            else:
                print("Invalid Command")
                print("Type 'help' for a list of commands")
