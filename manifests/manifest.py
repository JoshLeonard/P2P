from manifests.manifestfile import ManifestFile
import json

class Manifest:

    def __init__(self, file):
        self.file = file
        self.manifestfile = None

    def openmanifest(self, filepath):
        self.file.set_file_path(filepath)
        self.file.open()
        contents = self.file.get_contents()
        jsondictcontents = json.loads(contents)
        self.manifestfile = ManifestFile(**jsondictcontents)
        self.file.close()
        return self.manifestfile

