from file import File


class Segment:

    def __init__(self, segment_id, manifest_file):
        self.segment_id = segment_id
        self.manifest_file = manifest_file
        self.data = None
        self.file = None

    def attach_data(self, data):
        self.data = data

    def save(self):
        self.file = File(self.manifest_file.title + '.' + str(self.segment_id))
        self.file.open('wb')
        self.file.write(self.data)
        self.file.close()

    def get_segment(self):
        file = File('')
