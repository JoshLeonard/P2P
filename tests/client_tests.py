import unittest
from clientfilerequest import ClientFileRequest
from unittest.mock import MagicMock
from unittest.mock import Mock
from client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.mock_socket = Mock()
        decode = Mock()
        decode.decode = Mock(return_value='decode')
        self.mock_socket.recv = Mock(return_value=decode)
        self.client = Client(self.mock_socket)

    def test_client_can_instantiate(self):
        client = Client(Mock())
        self.assertIsInstance(client, Client, "None correct type")

    def test_client_connects_to_socket(self):
        self.client.connect()
        assert self.mock_socket.connect.called

    def test_client_processes_request_sends_file_request(self):
        request = ClientFileRequest('69ce09478b60b3853fda83e0cf2a3689')
        self.client.process(request)

        self.mock_socket.send.assert_called_with(b'file 69ce09478b60b3853fda83e0cf2a3689')

    def test_client_processes_request_receives_file_ack(self):
        request = ClientFileRequest('69ce09478b60b3853fda83e0cf2a3689')
        decode = Mock()
        decode.decode = Mock(return_value='ack file 69ce09478b60b3853fda83e0cf2a3689')
        self.mock_socket.recv = Mock(return_value=decode)
        self.client.process(request)





if __name__ == "__main__":
    unittest.main()