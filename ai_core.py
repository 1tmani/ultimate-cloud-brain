def decide(command):
    if "hello" in command:
        return "Hello from AI core"
    if "status" in command:
        return "AI reports stable"
    if "analyze" in command:
        return "AI analyzing command deeply"
    return f"AI processed: {command}"
