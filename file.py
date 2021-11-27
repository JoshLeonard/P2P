import math
import os


class File:

    def __init__(self, filepath = None, chunksize = 1024):
        self.filepath = filepath
        self.file = None
        self.chunksize = chunksize
        self.contents = None

    def set_file_path(self, filepath):
        self.filepath = filepath

    def open(self, open_type = 'r'):
        self.file = open(self.filepath, open_type)

    def write(self, data):
        self.file.write(data)

    def get_contents(self):
        self.file.seek(0)
        self.contents = self.file.read()
        return self.contents

    def file_chunk_count(self):
        size = self.file.seek(0, os.SEEK_END)
        return math.ceil(size / self.chunksize)

    def close(self):
        self.file.close()
