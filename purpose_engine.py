def purpose():
    return "Create, improve, validate, and prepare systems autonomously"

def mission(command):
    if "build" in command:
        return "Creation priority"
    if "learn" in command:
        return "Learning priority"
    if "deploy" in command:
        return "Deployment priority"
    if "grow" in command:
        return "Expansion priority"
    return "General intelligence priority"
