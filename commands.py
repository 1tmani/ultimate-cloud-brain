from task_router import route

def execute(command):
    parts = command.split(",")
    results = []
    for part in parts:
        results.append(route(part.strip()))
    return " | ".join(results)
