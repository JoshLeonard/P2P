import os


class CommandProcessor:

    def __init__(self, get_command, send_command):
        self.get_command = get_command
        self.send_command = send_command
        self.currentCommand = 0

    def process_segment_command(self, command):
        i = 1
        segments = []
        segment_id = command[i]
        while segment_id != '-f':
            segments.append(segment_id)
            i += 1
            segment_id = command[i]
        return segments

    def process_file_command(self, command):
        file = command[1]
        path = '/Users/Josh/PycharmProjects/pythonProject/shared/'
        file_path = os.path.join(path, file)
        return os.path.exists(file_path)

