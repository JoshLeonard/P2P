import socket
import threading
from connectedpeer import ConnectedPeer


class Server:

    def __init__(self):
        self.connected_peers = []
        self.socket = None

    def create_connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        port = 12345
        self.socket.bind(('', port))
        self.socket.listen(5)

    def connection_loop(self, manifest_file = None):
        c, addr = self.socket.accept()
        connected_peer = ConnectedPeer(c, manifest_file)
        th = threading.Thread(target=Server.handle_connection, args=(connected_peer, ))
        self.connected_peers.push((connected_peer, th))
        th.start()

    @staticmethod
    def handle_connection(connected_peer):
        connected_peer.process()


