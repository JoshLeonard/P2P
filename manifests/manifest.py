from manifests.manifestfile import ManifestFile
import json


class Manifest:

    def get_manifest(self, filepath):
        file = open(filepath, 'r')
        contents = file.read()
        json_dict_contents = json.loads(contents)
        file.close()
        return ManifestFile(**json_dict_contents)

