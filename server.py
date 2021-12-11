import socket
import threading
from peerconnectionfactory import PeerConnectionFactory


class Server:
    PeerConnectionFactoryClass = PeerConnectionFactory

    def __init__(self):
        self.connected_peers = []
        self.socket = None
        self.peer_connection_factory = self.PeerConnectionFactoryClass()

    def create_connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        port = 12345
        self.socket.bind(('', port))
        self.socket.listen(5)

    def connection_loop(self):
        c, addr = self.socket.accept()
        connected_peer = self.peer_connection_factory.create_peer_connection(c)
        th = threading.Thread(target=connected_peer.process(), args=(connected_peer, ))
        self.connected_peers.append((connected_peer, th))
        th.start()



