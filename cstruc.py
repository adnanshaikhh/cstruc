r"""
cstruc is a command line tool to visualize your C++ project structure
Usage:
cstruc open <folder-path>
cstruc (-h | --help)
cstruc
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

__version__ = "0.0.1"

def open_folder(folder_path):
    '''
    Opens the folder

    Args:
        folder_path: Path to the C++ folder

    Returns:
        None
    '''
    pass

def main():
    '''
    Parses the arguments

    Args:
        None

    Returns:
        None
    '''
    arguments = docopt(__doc__, version=__version__)
    if arguments['open']:
        open_folder(arguments['<folder-path'])
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
