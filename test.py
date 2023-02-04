#!/usr/bin/python3
"""Testing things out """
from fabric.api import *

def list_directory(archive_folder):
    result = local('ls versions/', capture=True)
    print(result.split('\n'))
