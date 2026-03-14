import os

def validate_project(folder):
    if os.path.exists(folder) and len(os.listdir(folder)) > 0:
        return "Validation success"
    return "Validation failed"
