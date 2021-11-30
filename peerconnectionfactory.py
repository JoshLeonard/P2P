from connectedpeer import ConnectedPeer
from segmentloader import SegmentLoader


class PeerConnectionFactory:

    def create_peer_connection(self, connection):
        return ConnectedPeer(connection, SegmentLoader())
