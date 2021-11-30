import socket
from clientfilerequest import ClientFileRequest


class Client:

    def __init__(self, s):
        self.socket = s

    def connect(self, ip_address=None, port=12345):
        if ip_address is None:
            ip_address = '127.0.0.1'
        self.socket.connect((ip_address, port))

    def process(self, manifest_file, send_data):
        ip_address = manifest_file.ip_addresses[0]
        self.connect(ip_address)
        self.request_file(manifest_file)
        segment_id = self.request_segment_contract(manifest_file)
        print('client: received segment id')
        self.receive_data(manifest_file, segment_id, send_data)

    def request_file(self, request):
        file_command = "file " + request.file_hash
        self.socket.send(file_command.encode())
        print('sending file command')
        result = self.socket.recv(500).decode()
        print('receiving result: ' + result)
        if 'ack' not in result:
            return False
        return True

    def request_segment_contract(self, manifest_file):
        self.socket.send('segments 1 2 3 4 5 6 7 8 9 -f'.encode())
        print('sending segment command')
        result = self.socket.recv(500).decode()
        print('receiving result ' + result)
        split_result = result.split()
        if not self.check_segment_available(split_result[2]):
            raise Exception("requested segment is not available!")
        self.socket.send('ack segment contract 6'.encode())
        command = 'segment ' + manifest_file.file_hash + ' ' + split_result[2]
        print('sending command: ' + command)
        self.socket.send(command.encode())
        return split_result[2]

    def receive_data(self):
        result = self.socket.recv(500).encode()
        if result == 'data':
            print('receiving data')
            self.receive_data()

    def receive_data(self, manifest_file, segment_id, send_data):
        bytes = self.receive_bytes()
        send_data(manifest_file.file_hash, segment_id, bytes)

    def check_segment_available(self, segment_id):
        return True

    def receive_bytes(self):
        bytes = self.socket.recv(1048576)
        return bytes
