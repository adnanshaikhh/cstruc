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
import sys
import graph
import traverse
import serve

__version__ = "0.0.1"

def construct_json(graph_json):
    settings = dict(initialDegree=0.1)

    return dict(settings=settings, graph=graph_json)

def open_folder(folder_path):
    '''
    Opens the folder

    Args:
        folder_path: Path to the C++ folder

    Returns:
        None
    '''
    c_graph = graph.Graph()

    traverse.traverse(c_graph, folder_path)

    if c_graph.is_empty():
        print "Graph is empty!"
        sys.exit(-1)

    print c_graph

    json = construct_json(c_graph.to_json())

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
        open_folder(arguments['<folder-path>'])
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
