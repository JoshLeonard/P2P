import math
import os

class File:

    def __init__(self, filepath = None, chunksize = 1024):
        self.filepath = filepath
        self.file = None
        self.chunksize = chunksize
        self.contents = None

    def setfilepath(self, filepath):
        self.filepath = filepath

    def open(self):
        self.file = open(self.filepath, 'r')

    def getcontents(self):
        self.file.seek(0)
        self.contents = self.file.read()
        return self.contents

    def fileChunkCount(self):
        size = self.file.seek(0, os.SEEK_END)
        return math.ceil(size / self.chunksize)

    def close(self):
        self.file.close()
