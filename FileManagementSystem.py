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
        self.directories = {}
        self.directories["root"] = self.root

    def create_file(self, name):
        file = File(name)
        self.files[name] = file
        self.current_directory.add_file(file)

    def create_directory(self, name):
        directory = Directory(name)
        self.directories[name] = directory
        self.current_directory.add_subdirectory(directory)

    def delete_file(self, name):
        current_directory = self.current_directory
        for file in current_directory.files:
            if file.name == name:
                current_directory.remove_file(file)
                self.files.pop(name)
                return

    def append_file(self, name, data):
        print(name)
        file = self.files[name]
        file.append(data, self.Memory)

    def change_directory(self, name):
        if name == "..":
            self.current_directory = self.current_directory.parent
        else:
            self.current_directory = self.directories[name]

    def MemoryMap(self):
        for i in self.directories:
            print("Directory: " + i)
            for j in self.directories[i].files:
                print("  File: " + str(j))
                for k in j.blocks:
                    print("     " + str(k))

    def save(self):
        with open("file_system.pickle", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        with open("file_system.pickle", "rb") as file:
            return pickle.load(file)
