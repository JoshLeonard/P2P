

class ConnectedPeer:

    def __init__(self, connection, manifestfile):
        self.connection = connection
        self.manifestfile = manifestfile

    def process(self):
        while True:
            commandChunk = self.connection.recv(500)
            command = commandChunk.decode()
            commandSplit = command.split()
            if commandSplit[0] == 'file':
                print(commandSplit[1])
            elif commandSplit[0] == 'segments':
                i = 1
                next = commandSplit[i]
                while next != '-f':
                    print(next)
                    i += 1
                    next = commandSplit[i]