class Log:
    def __init__(self, log_file):
        self.log_file = log_file

    def write(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')