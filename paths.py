'''Handles searching for the WWW path and copying operations.'''

import os
import shutil
import tempfile

WWW = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'www')

if not os.path.exists(WWW):
    message = 'Could not find www directory for ig: {0}'
    raise EnvironmentError(message.format(WWW))


def create_directory(directory):
    if directory is None:
        directory = tempfile.mkdtemp(prefix='cstruct-')
        print('Created temporary directory %s', directory)

    # Has to not exist for copytree
    if os.path.exists(directory):
        shutil.rmtree(directory)

    shutil.copytree(WWW, directory)

    print('Copied contents of www folder to %s', directory)

    return directory
