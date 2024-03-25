import os

def repo_path():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    return parent_dir

