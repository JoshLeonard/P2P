from manifests.manifest import Manifest
from file import File


class SegmentLoader:

    def get_contents_by_segment(self, file_hash, segment_id):
        segment_size = 1024*1024
        f = File('/Users/Josh/PycharmProjects/pythonProject/shared/' + file_hash + '/manifest.json')
        manifest = Manifest(f)
        manifest_file = manifest.openmanifest('/Users/Josh/PycharmProjects/pythonProject/shared/'
                                              + file_hash + '/manifest.json')
        file = open('/Users/Josh/PycharmProjects/pythonProject/shared/' + file_hash + '/' + manifest_file.filename, 'rb')
        start_byte = (segment_id - 1) * segment_size
        file.seek(start_byte)
        segment_data = file.read(segment_size)
        return segment_data