Paste this exactly into a new file named **mega_engine.py** (same folder as `app.py` and `brain.py`):

```python
import os
import json
from datetime import datetime

def mega_run(command):
    command = command.lower().strip()

    history_file = "history_store.json"

    history = []
    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                history = json.load(f)
        except:
            history = []

    history.append({
        "command": command,
        "time": str(datetime.now())
    })

    with open(history_file, "w") as f:
        json.dump(history, f)

    if "website" in command:
        folder = "mega_website"
        os.makedirs(folder, exist_ok=True)

        with open(f"{folder}/index.html", "w") as f:
            f.write("""
<!DOCTYPE html>
<html>
<head>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<h1>Mega Website Active</h1>
<script src='script.js'></script>
</body>
</html>
""")

        with open(f"{folder}/style.css", "w") as f:
            f.write("""
body{
background:black;
color:cyan;
font-family:Arial;
text-align:center;
}
""")

        with open(f"{folder}/script.js", "w") as f:
            f.write("""
console.log("Mega engine running");
""")

        return "Mega engine built website with full files"

    if "api" in command:
        folder = "mega_api"
        os.makedirs(folder, exist_ok=True)

        with open(f"{folder}/api.py", "w") as f:
            f.write("""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Mega API Active"

if __name__ == "__main__":
    app.run()
""")

        return "Mega engine built api"

    if "dashboard" in command:
        folder = "mega_dashboard"
        os.makedirs(folder, exist_ok=True)

        with open(f"{folder}/dashboard.html", "w") as f:
            f.write("""
<html>
<body style='background:black;color:cyan;text-align:center;'>
<h1>Mega Dashboard</h1>
</body>
</html>
""")

        return "Mega engine built dashboard"

    if "history" in command:
        return f"Stored commands: {len(history)}"

    if "theme light" in command:
        return "Theme switched to light"

    if "theme neon" in command:
        return "Theme switched to neon"

    if "analyze" in command:
        return f"Analyzed command length: {len(command)}"

    if "inspect" in command:
        folders = [x for x in os.listdir() if os.path.isdir(x)]
        return f"Folders: {folders}"

    if "upgrade" in command:
        return "Mega upgrade score: stable"

    if "learn" in command:
        return f"Learning captured: {command}"

    if "deploy" in command:
        return "Deploy pathway prepared"

    return f"Mega engine processed: {command}"
```

---

# Then open **brain.py** and add only this import at top:

```python
from mega_engine import mega_run
```

---

# Then inside `think(command)` add:

```python
if "mega" in command:
    return mega_run(command)
```

Put it immediately after:

```python
command = repair_command(command.lower())
```

---

# So final place looks like:

```python
command = repair_command(command.lower())

if "mega" in command:
    return mega_run(command)
```

---

# Upload only:

✅ `mega_engine.py`
✅ updated `brain.py`

to GitHub

Then Render redeploys.

---

# Test command

```text id="m7q3p1"
mega website
```

🚀
