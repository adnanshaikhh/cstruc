'''Traverses the folder structure of the project'''

from __future__ import print_function

import fnmatch
import logging
import os
import re
import sys

include_pattern = re.compile(r'^#include ["<](.*)[">]$')

def try_prefixes(path, prefixes):
    for prefix in prefixes:
        full_path = os.path.realpath(os.path.join(prefix, path))
        if os.path.exists(full_path):
            return full_path

    return path


def get_includes(filename, prefixes):
    includes = set()
    with open(filename) as source:
        for line in source:
            match = include_pattern.match(line)
            if match is not None:
                full_path = try_prefixes(match.group(1), prefixes)
                includes.add(full_path)
    return includes

def glob(folder_name, pattern):
    for root, _, filenames in os.walk(folder_name):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)

def traverse(graph, folder_path):
    for pattern in ['*.[ch]pp', '*.[ch]']:
        path = os.path.realpath(folder_path)
        for filename in glob(path, pattern):
            if os.path.isdir(filename):
                continue
            includes = get_includes(filename, [path] + [os.getcwd()])
            graph.add(filename, includes)

