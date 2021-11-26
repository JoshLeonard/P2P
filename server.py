import socket
import threading
from connectedpeer import ConnectedPeer

class Server:

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        port = 12345
        self.s.bind(('', port))
        self.s.listen(5)

    def connection_loop(self, manifestfile = None):
        c, addr = self.s.accept()
        print(addr)
        th = threading.Thread(target=Server.handleconnection, args=(c, manifestfile))
        th.start()

    @staticmethod
    def handleconnection(connection, manifestfile):
        connectedpeer = ConnectedPeer(connection, manifestfile)
        connectedpeer.process()


