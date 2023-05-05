from Log import Log

class User:
    def __init__(self, name):
        self.name = name
        self.log = Log(f"user_commands/logs/{name}_log.txt")
    
    def runCommands(self, inputFile, fileManagementSystem):
        with open(inputFile, 'r') as f:
            commands = f.readlines()
            for command in commands:
                self.log.write("\nExecuting: " + command)
                command = command.strip()
                if command == "exit":
                    break
                else:
                    fileManagementSystem.execute(command, self.log)
