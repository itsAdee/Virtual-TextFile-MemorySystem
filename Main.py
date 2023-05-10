from FileManagementSystem import *
from User import User
import threading

file_system = FileManagementSystem()


def create_file_system():
    print("Creating new file system...\n")
    file_system.create_file("fileInRoot.txt")
    file_system.create_directory("dir1")
    file_system.change_directory("dir1")
    file_system.create_file("fileInDir1.txt")
    file_system.create_directory("dir2")
    file_system.change_directory("dir2")
    file_system.create_file("fileInDir2.txt")

    file_system.write_file("fileInDir2.txt", "Hello World")

    file_system.save()


def createUserThread(user_name):
    user = User(user_name)
    user.runCommands(f"user_commands/{user_name}_input.txt", file_system)


if __name__ == "__main__":
    if os.path.exists("file_system.pickle"):
        print("Loading file system...\n")
        file_system = file_system.load()

    else:
        create_file_system()

    # Create multiple users on different threads
    input = input("Enter the number of threads to create: ")
    input = int(input)
    users = []
    for i in range(input):
        users.append(f"user{i}")
    threads = []
    for user in users:
        t = threading.Thread(target=createUserThread, args=(user,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("Saving file system...\n")
    print("File system saved.\n")
    file_system.save()

    # users = ["user1", "user2", "user3"]
    # threads = []
    # for user in users:
    #     t = threading.Thread(target=createUserThread, args=(user,))
    #     threads.append(t)
    #     t.start()

    # for t in threads:
    #     t.join()

    # file_system.save()
