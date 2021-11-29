# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from server import Server
from file import File
from manifests.manifest import Manifest
from connectedpeer import ConnectedPeer
from peerconnectionfactory import PeerConnectionFactory

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sharing = None
    server = None
    if len(sys.argv) > 0:
        sharing = sys.argv[1]

    if sharing == '-h':
        server = Server(PeerConnectionFactory())
        server.create_connection()


    f = File('/Users/Josh/downloads/manifest.json', 1024*1024)
    manifest = Manifest(f)
    manifest.openmanifest('/Users/Josh/downloads/manifest.json')

    if server is not None:
        server.connection_loop(manifest.manifestfile)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
