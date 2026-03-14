import os

def read_project(folder):
    if os.path.exists(folder):
        return ", ".join(os.listdir(folder))
    return "Project folder not found"
