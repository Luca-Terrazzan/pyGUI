"""This module handles all needed file reading operations
"""
from typing import List
import os

class FolderReader:
    """This class handles all needed folder reading operations
    """

    # The main path on which this folder reader instance operates
    path: str

    def __init__(self, path: str) -> None:
        """Attach a folder reader to a folder
        """
        if not os.path.exists(path):
            raise TypeError('Invalid path!')
        self._path = path

    def get_folder_content(self) -> List[str]:
        """Reads a folder content and returns a list of filenames

        Returns:
            str: [description]
        """
        return os.listdir(self._path)

inst = FolderReader(path='/Users/luca.terrazzan/Documents/workspace/pyGUI')
print(inst.get_folder_content())
