class CommandProcessor:

    def process_command(self, command):
        return None

    @staticmethod
    def process_segment_command(command):
        i = 1
        next = command[i]
        while next != '-f':
            print(next)
            i += 1
            next = command[i]

    @staticmethod
    def process_file_command(command):
        print(command[1])

