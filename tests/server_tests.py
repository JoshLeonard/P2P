import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch
import server


class TestServer(unittest.TestCase):

    def setUp(self):

        peerconnectionfactory = Mock()
        self.connectedpeer = Mock()
        peerconnectionfactory.create_peer_connection = MagicMock(return_value=self.connectedpeer)
        self.server = server.Server(peerconnectionfactory)
        self.server.socket = Mock()
        self.server.socket.accept = MagicMock(return_value=(Mock(), '127.0.0.1'))

    def test_upper(self):
        self.server.connection_loop(None)
        assert self.server.socket.accept.called
        assert self.server.peer_connection_factory.create_peer_connection.called
        assert self.connectedpeer.process.called

if __name__ == '__main__':
    unittest.main()