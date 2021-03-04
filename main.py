import os
import zipfile


def unzip(path, z_path):
    z_file = zipfile.ZipFile(z_path, 'r')
    for name in z_file.namelist():
        dir_, file = os.path.split(name)
        if not os.path.exists(path + os.sep + dir_):
            os.mkdir(path + os.sep + dir_)
        if file:
            handler = open(path + os.sep + name, 'wb')
            handler.write(z_file.read(name))
            handler.close()
    z_file.close()


unzip('unarchive_folder', 'archive.zip')
