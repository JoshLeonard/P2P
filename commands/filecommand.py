import os
from basecommand import BaseCommand


class FileCommand(BaseCommand):

    def __init__(self, get_command, send_command):
        super.__init__(get_command, send_command)

    def process_command(self):
        command = self.get_command()
        file = command[1]
        path = '/Users/Josh/PycharmProjects/pythonProject/shared/'
        file_path = os.path.join(path, file)
        return os.path.exists(file_path)