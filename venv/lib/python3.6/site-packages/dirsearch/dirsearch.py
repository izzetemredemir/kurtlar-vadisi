import fnmatch
import os
import re


def dirsearch(path, extension='*.*', recursive=True):
    if not os.path.isdir(path):
        raise Exception('Invalid directory specified: {}'.format(path))

    rule = re.compile(fnmatch.translate(extension), re.IGNORECASE)
    if recursive:
        return list([os.path.join(x[0], y) for x in os.walk(path) for y in os.listdir(x[0]) if rule.match(y)])
    else:
        return [name for name in os.listdir(path) if rule.match(name)]