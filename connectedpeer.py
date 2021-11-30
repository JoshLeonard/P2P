import random

from commands.CommandProcessor import CommandProcessor
from segment import Segment
from segmentloader import SegmentLoader


class ConnectedPeer:

    def __init__(self, connection, segment_loader):
        self.connection = connection
        self.connected = True
        self.segments = None
        self.command_processor = CommandProcessor(self.get_command, self.send_command)
        self.segment_loader = segment_loader
        self.file_hash = None

    def process(self):
        while self.connected:
            command = self.get_command()
            self.process_command(command)
        self.connection.close()

    def process_command(self, command):
        print(command[0] + " received")
        if command[0] == 'file':
            self.process_file_command(command)
        elif command[0] == 'segments':
            print('server: received segments command')
            self.process_segments_command(command)
        elif command[0] == 'segment':
            print('server: received segment command')
            self.process_segment_command(command)

    def process_segment_command(self, command):
        file_hash = command[1]
        segment_id = command[2]
        file_segment = self.segment_loader.get_contents_by_segment(file_hash, segment_id)
        self.connection.send('data'.encode())
        self.connection.send(file_segment)

    def process_segments_command(self, command):
        self.segments = self.command_processor.process_segment_command(command)
        selected_segment = self.select_random_segment()
        self.send_command('segment contract ' + selected_segment)

    def process_file_command(self, command):
        if self.command_processor.process_file_command(command):
            self.send_command("ack file " + command[1])
            self.file_hash = command[1]
        else:
            self.send_command('failed file')
            self.connected = False

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
        received_bytes = self.connection.recv(1048576)
        return received_bytes
