import os

def execute_file(path):
    if os.path.exists(path):
        return open(path).read()
    return "Execution target not found"
