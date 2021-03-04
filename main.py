import zipfile


def unzip(path, z_path):
    z_file = zipfile.ZipFile(z_path, 'r')


unzip(path, z_path)
