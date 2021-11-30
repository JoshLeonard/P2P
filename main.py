# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import threading
import socket

from client import Client
from server import Server
from userinterface import UserInterface
from services.fileservice import FileService
from peerconnectionfactory import PeerConnectionFactory


def run_server(args):
    if args == '-h':
        print('creating server')
        server = Server(PeerConnectionFactory())
        server.create_connection()

    if server is not None:
        print('starting server')
        server.connection_loop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sharing = None
    if len(sys.argv) > 0:
        sharing = sys.argv[1]

    th = threading.Thread(target=run_server, args=(sharing,))
    th.start()

    client = Client(socket.socket())
    file_service = FileService(client)
    ui = UserInterface(file_service)
    ui.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
