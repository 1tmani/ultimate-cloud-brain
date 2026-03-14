import json, os
FILE = "history_store.json"

def save_command(command):
    history = []
    if os.path.exists(FILE):
        history = json.load(open(FILE))
    history.append(command)
    json.dump(history, open(FILE,"w"))

def load_history():
    if os.path.exists(FILE):
        return json.load(open(FILE))
    return []
