
import os
import platform

__author__ = 'John O\'Connor'
__version__ = '0.1'

def which(cmd):
# based on solutions from
# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    def is_executable(path):
        return os.path.exists(path) and os.access(path, os.X_OK)

    if platform.system() == 'Windows':
        def possible_file_extensions(path):
            yield path
            for ext in os.environ.get('PATHEXT', '').split(os.pathsep):
                yield path + ext
    else:
        def possible_file_extensions(path):
            yield path

    path, name = os.path.split(cmd)
    if path:
        if is_executable(cmd):
            return cmd
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            cmd_file = os.path.join(path, cmd)
            for candidate in possible_file_extensions(cmd_file):
                if is_executable(candidate):
                    return candidate

    return None

