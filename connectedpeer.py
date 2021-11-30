import random

from commands.CommandProcessor import CommandProcessor
from segment import Segment
from segmentloader import SegmentLoader


class ConnectedPeer:

    def __init__(self, connection, segment_loader):
        self.connection = connection
        self.current_segment_id = 1
        self.connected = True
        self.segments = None
        self.command_processor = CommandProcessor(self.get_command, self.send_command)
        self.file_hash = None
        self.segment_loader = segment_loader

    def process(self):
        while self.connected:
            command = self.get_command()
            if command[0] == 'file':
                if self.command_processor.process_file_command(command):
                    self.send_command("ack file " + command[1])
                    self.file_hash = command[1]
                else:
                    self.send_command('failed file')
                    self.connected = False
            elif command[0] == 'segments':
                self.segments = self.command_processor.process_segment_command(command)
                selected_segment = self.select_random_segment()
                self.send_command('segment contract ' + selected_segment)
            elif command[0] == 'segment':
                file_hash = command[1]
                segment_id = command[2]
                file_segment = self.segment_loader.get_contents_by_segment(file_hash, segment_id)
                self.connection.send(file_segment)

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