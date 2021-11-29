import random

from commands.CommandProcessor import CommandProcessor
from segment import Segment


class ConnectedPeer:

    def __init__(self, connection, manifest_file):
        self.connection = connection
        self.manifest_file = manifest_file
        self.current_segment_id = 1
        self.connected = True
        self.segments = None
        self.command_processor = CommandProcessor(self.get_command, self.send_command)

    def process(self):
        while self.connected:
            command = self.get_command()
            if command[0] == 'file':
                if self.command_processor.process_file_command(command):
                    self.send_command("ack file " + command[1])
                else:
                    self.send_command('failed file')
                    self.connected = False
            elif command[0] == 'segments':
                self.segments = self.command_processor.process_segment_command(command)
                selected_segment = self.select_random_segment()
                self.send_command('segment contract ' + selected_segment)
            elif command[0] == 'data':
                bytes = self.receive_bytes()
                segment = Segment(self.current_segment_id, self.manifest_file)
                segment.attach_data(bytes)
                segment.save()
            elif command[0] == ''

    def select_random_segment(self):
        segment_count = len(self.segments)
        selected_segment = int(random.random() * segment_count)
        return self.segments[selected_segment]

    def get_command(self):
        command_chunk = self.connection.recv(500)
        command = command_chunk.decode()
        return command.split()

    def send_command(self, command):
        self.connection.send(command.encode())

    def receive_bytes(self):
        bytes = self.connection.recv(1048576)
        return bytes