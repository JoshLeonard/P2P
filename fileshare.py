import os
import hashlib
import shutil
import json
from manifests.manifestfile import ManifestFile

print("Enter the path to the file:")
path = input()

f = open(path, 'rb')
size = f.seek(0, os.SEEK_END)
f.seek(0)

hexHash = hashlib.md5(f.read()).hexdigest()
f.seek(0)

directory = str(hexHash)
parent_directory = '/Users/Josh/PycharmProjects/pythonProject/shared'
new_path = os.path.join(parent_directory, directory)
os.mkdir(new_path)

filename = os.path.basename(f.name)
manifest_file = ManifestFile(filename, size, hexHash, filename, ['127.0.0.1'])
manifest_file_json = json.dumps(manifest_file, default=lambda o: o.__dict__, sort_keys=True, indent=4)

shutil.copy2(path, new_path)

newFilePath = os.path.join(new_path, 'manifest.json')
manifest_file_json_file = open(newFilePath, 'w')
manifest_file_json_file.write(manifest_file_json)
manifest_file_json_file.close()
f.close()

