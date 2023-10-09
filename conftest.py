import shutil
import zipfile

import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    os.mkdir('tmp')
    root = os.path.dirname(__file__)
    path = os.path.join(root, 'resources/')
    file_dir = os.listdir(path)
    with zipfile.ZipFile('tmp/test.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file, arcname=file)

    yield
    pass
    os.remove('tmp/test.zip')
    os.rmdir('tmp')
