from abc import ABC, abstractmethod


class BaseCommand(ABC):

    def __init__(self, get_command, send_command):
        self.get_command = get_command
        self.send_command = send_command

    @abstractmethod
    def process_command(self):
        pass
