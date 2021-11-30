from manifests.manifest import Manifest
from segment import Segment


class FileService:

    def __init__(self, client):
        self.client = client

    def file_request(self, path):
        manifest_file = self.load_manifest(path)
        self.client.process(manifest_file, self.receive_file_data)

    def load_manifest(self, path):
        manifest = Manifest()
        return manifest.get_manifest(path)

    def receive_file_data(self, manifest_file, current_segment_id, data):
        segment = Segment(current_segment_id, manifest_file)
        print('segment created')
        segment.attach_data(bytes)
        print('saving segment')
        segment.save()