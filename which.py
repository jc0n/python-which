"""
Python implementation of Unix `which` command.
"""

import os
import platform

__author__ = 'John O\'Connor'
__version__ = '0.1.2'

__all__ = ('CommandNotFoundException', 'which')

class CommandNotFoundException(Exception):
    """Raised when `which` fails to locate a proper command path."""

if platform.system() == 'Windows':
    def possible_file_extensions(path):
        yield path
        for ext in os.environ.get('PATHEXT', '').split(os.pathsep):
            yield path + ext
else:
    def possible_file_extensions(path):
        yield path

def is_executable(path):
    return os.path.exists(path) and os.access(path, os.X_OK)

# Based on solutions from
# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(cmd, extra_paths=()):
    path, name = os.path.split(cmd)
    if path:
        if is_executable(cmd):
            return cmd
    else:
        paths = os.environ['PATH'].split(os.pathsep)
        if extra_paths:
            from itertools import chain
            paths = chain.from_iterable(extra_paths, paths)
        for path in paths:
            if not (os.path.exists(path) and os.path.isdir(path)):
                continue
            cmd_file = os.path.join(path, cmd)
            for candidate in possible_file_extensions(cmd_file):
                if is_executable(candidate):
                    return candidate

    raise CommandNotFoundException(cmd)

