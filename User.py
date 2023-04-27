from Log import Log

class User:
    def __init__(self, name):
        self.name = f"User_{name}"
        self.log = Log(f"{name}_log.txt")
    
    def runCommands(self, inputFile, fileManagementSystem):
        with open(inputFile, 'r') as f:
            commands = f.readlines()
            for command in commands:
                self.log.write("Executing: " + command + "\n")
                command = command.strip()
                if command == "exit":
                    break
                else:
                    fileManagementSystem.execute(command, self.log)
