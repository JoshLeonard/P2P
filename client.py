import socket
from clientfilerequest import ClientFileRequest
from segment import Segment


class Client:

    def __init__(self, s):
        self.socket = s

    def connect(self, ip_address=None, port=12345):
        if ip_address is None:
            ip_address = '127.0.0.1'
        self.socket.connect((ip_address, port))

    def process(self, request):
        self.request_file(request)
        self.request_segment_contract()
        self.receive_data()

    def request_file(self, request):
        file_command = "file " + request.hash
        self.socket.send(file_command.encode())
        print('sending file command')
        result = self.socket.recv(500).decode()
        print('receiving result: ' + result)
        if 'ack' not in result:
            return False
        return True

    def request_segment_contract(self):
        self.socket.send('segments 1 2 3 4 5 6 7 8 9 -f'.encode())
        print('sending segment command')
        result = self.socket.recv(500).decode()
        print('receiving result ' + result)
        split_result = result.split()
        if not self.check_segment_available(split_result[2]):
            return False
        self.socket.send('ack segment contract 6'.encode())
        return True

    def receive_data(self):
        result = self.socket.recv(500).encode()
        if result == 'data':
            print('receiving data')
            self.receive_data()

    def receive_data(self):
        bytes = self.receive_bytes()
        segment = Segment(self.current_segment_id, self.manifest_file)
        print('segment created')
        segment.attach_data(bytes)
        print('saving segment')
        segment.save()

    def check_segment_available(self, segment_id):
        return True

    def receive_bytes(self):
        bytes = self.socket.recv(1048576)
        return bytes

if __name__ == "__main__":
    c = Client(socket.socket())
    c.connect()
    request = ClientFileRequest('69ce09478b60b3853fda83e0cf2a3689')
    c.process(request)