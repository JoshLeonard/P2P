from connectedpeer import ConnectedPeer


class PeerConnectionFactory:

    def create_peer_connection(self, connection, manifest_file):
        return ConnectedPeer(connection, manifest_file)
