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

    def create_file(self, name, log):
        if name in self.files:
            log.write("File Creation Failed: File already exists")
            return
        file = File(name)
        self.files[name] = file
        self.current_directory.add_file(file)

    def create_directory(self, name, log):
        directoryPath = name.split("/")
        current_directory = self.current_directory
        for i in directoryPath:
            if i == "":
                continue
            for directory in current_directory.subdirectories:
                if directory.name == i:
                    current_directory = directory
                    break
        if directoryPath[-1] == "":
            directory = Directory(directoryPath[-2])
        else:
            directory = Directory(directoryPath[-1])
        log.write("Directory Creation Successful")

        current_directory.add_subdirectory(directory)
        self.subdirectories[name] = directory

    def delete_file(self, name, log):
        current_directory = self.current_directory
        for file in current_directory.files:
            if file.name == name:
                current_directory.remove_file(file)
                self.files.pop(name)
                return
            else:
                log.write("File Deletion Failed: File does not exist")

    def delete_directory(self, directoryName, log):
        try:
            directoryPath = directoryName.split("/")

            current_directory = self.current_directory
            for i in directoryPath:
                if i == "":
                    continue
                for directory in current_directory.subdirectories:
                    if directory.name == i:
                        current_directory = directory
                        break
            for file in current_directory.files:
                file.delete(self.Memory)
            current_directory.parent.subdirectories.remove(current_directory)
            log.write("Directory Deletion Successful")

        except:
            print("directory not found")

    def append_file(self, name, data, log):
        try:
            file = self.files[name]
            file.append(data, self.Memory, log)
        except:
            log.write("File Append Failed: File does not exist")

    def write_file(self, name, data, log):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            my_file.write(data, self.Memory, log)
            return my_file
        except:
            log.write("File Write Failed: File does not exist")

    def truncate_file(self, name, size, log):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            my_file.truncatefile(self.Memory, size, log)
        except:
            log.write("File Truncate Failed: File does not exist")

    def readFile(self, name, log):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(name)
            return my_file.read(self.Memory, log)
        except:
            log.write("File Read Failed: File does not exist")

    def MoveContent(self, name, start, end, newstart, log):
        current_directory = self.current_directory
        my_file = current_directory.find_file(name)
        my_file.moveContentWithinFile(self.Memory, start, end, newstart, log)

    def memoryMap(self, current_directory=None, log=None):
        if current_directory is None:
            current_directory = self.root
            log.write("/")

        spaces = current_directory.level * 2
        for file in current_directory.files:
            blocks = ""
            for block in file.blocks:
                blocks += str(block) + ","
            log.write(" " * spaces + file.name + " " + str(file.id) +
                      " " + str(file.file_size) + " " + blocks)
        for directory in current_directory.subdirectories:
            if directory.name == self.current_directory.name:
                log.write(" " * spaces + "*" + directory.name + "/")
            else:
                log.write(" " * spaces + directory.name + "/")
            self.memoryMap(directory, log)

    def change_directory(self, name, log):
        if self.current_directory.parent == None and name == "..":
            return

        if name == "..":
            self.current_directory = self.current_directory.parent
            log.write("directory changed to " +
                      str(self.current_directory.name))
        else:
            pathToDirectory = name.split("/")
            for name in pathToDirectory:
                if name == "":
                    continue
                for directory in self.current_directory.subdirectories:
                    if directory.name == name:
                        self.current_directory = directory
                        log.write("directory changed to " +
                                  str(self.current_directory.name))
                        break

    def moveFileInDirectory(self, fileName, newDirectory, log):
        try:
            current_directory = self.current_directory
            my_file = current_directory.find_file(fileName)
            current_directory.remove_file(my_file)
        except:
            log.write("File Move Failed: File does not exist")
            return

        if newDirectory == "..":
            if current_directory.parent == None:
                return

            current_directory = current_directory.parent
            duplicate = current_directory.find_file(fileName)
            if duplicate != None:
                current_directory.remove_file(duplicate)
                log.write("Duplicate file found, deleting duplicate")
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
        duplicate = current_directory.find_file(fileName)
        if duplicate != None:
            current_directory.remove_file(duplicate)
            log.write("Duplicate file found, deleting duplicate")
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

    def save(self):
        with open("file_system.pickle", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        with open("file_system.pickle", "rb") as file:
            return pickle.load(file)

    def listAll(self, log):
        for i in self.current_directory.subdirectories:
            log.write(i.name + "/")
        for i in self.current_directory.files:
            log.write(i.name)

    def execute(self, prompt, log):
        prompt = prompt.split(" ")
        command = prompt[0]

        # List all files and directories: ls
        if command == "ls":
            log.write("Listing all files and directories: \n")
            self.listAll(log)
            log.write("\n")
            pass

        # Create a file (add to the directory): touch <filename>
        elif command == "touch":
            self.create_file(prompt[1], log)
            log.write("Created file: " + prompt[1])

        # Delete a file (remove from the directory): rm <filename>
        elif command == "rm":
            self.delete_file(prompt[1], log)
            log.write("Deleted file: " + prompt[1])
            pass

        # Write to a file (overwrite): wr <filename> <text>
        elif command == "wr":
            written_text = ""
            for i in range(2, len(prompt)):
                written_text += prompt[i] + " "
            self.write_file(prompt[1], written_text, log)
            log.write("Wrote to file: " + prompt[1])

        # Append to a file (add to the end): ap <filename> <text>
        elif command == "ap":
            appended_text = ""
            for i in range(2, len(prompt)):
                appended_text += prompt[i] + " "
            self.append_file(prompt[1], appended_text, log)
            log.write("Appended to file: " + prompt[1])

        # Truncate a file (remove content): tr <filename> <end bit>
        elif command == "tr":
            self.truncate_file(prompt[1], prompt[2], log)
            log.write("Truncated file: " + prompt[1])

        # Move content within a file: mvc <filename> <start> <size> <newstart/target>
        elif command == "mvc":
            self.MoveContent(prompt[1], int(
                prompt[2]), int(prompt[3]), int(prompt[4]), log)
            log.write("Moved content in file: " + prompt[1])

        # Read a file: cat <filename>
        elif command == "cat":
            log.write("Reading file: " + prompt[1])
            log.write(self.readFile(prompt[1], log))
            log.write("File read")
            pass

        elif command == "mmap":
            log.write("\nLogging Memory Map:")
            self.memoryMap(log=log)
            log.write("Logged Memory Map\n")
            pass

        # Save the file system: save
        elif command == "save":
            self.save()
            log.write("Saved file system")
