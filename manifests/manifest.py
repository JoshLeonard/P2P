from manifests.manifestfile import ManifestFile
import json

class Manifest:

    def __init__(self, file):
        self.file = file
        self.manifestfile = None

    def openmanifest(self, filepath):
        self.file.setfilepath(filepath)
        self.file.open()
        contents = self.file.getcontents()
        jsondictcontents = json.loads(contents)
        self.manifestfile = ManifestFile(**jsondictcontents)
        self.file.close()
        print('test')

