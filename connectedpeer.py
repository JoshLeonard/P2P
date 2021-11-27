from commands.CommandProcessor import CommandProcessor
from segment import Segment


class ConnectedPeer:

    def __init__(self, connection, manifest_file):
        self.connection = connection
        self.manifest_file = manifest_file

    def process(self):
        while True:
            command = self.get_command()
            if command[0] == 'file':
                CommandProcessor.process_file_command(command)
                self.connection.send("ack file".encode())
            elif command[0] == 'segments':
                CommandProcessor.process_segment_command(command)
                self.connection.send("ack segments".encode())
            elif command[0] == 'data':
                bytes = self.receive_bytes()
                segment = Segment(1, self.manifest_file)
                segment.attach_data(bytes)
                segment.save()

    def get_command(self):
        command_chunk = self.connection.recv(500)
        command = command_chunk.decode()
        return command.split()

    def receive_bytes(self):
        bytes = self.connection.recv(500)
        return bytes