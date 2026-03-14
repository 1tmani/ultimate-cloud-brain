from validator import validate_project
from project_reader import read_project

def automate(folder):
    status = validate_project(folder)
    files = read_project(folder)
    return f"{status} | Files: {files}"
