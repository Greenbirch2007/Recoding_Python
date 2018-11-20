# postimport.py



import importlib
import sys
from collections import defaultdict


_post_import_hooks = defaultdict[list]

class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self,fullname,path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return POs