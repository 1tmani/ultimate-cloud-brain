import os

def build_project(project_type="default"):
    folder = f"generated_{project_type}"
    os.makedirs(folder, exist_ok=True)

    if project_type == "website":
        open(f"{folder}/index.html","w").write("<!DOCTYPE html><html><body><h1>Generated Website</h1></body></html>")
        open(f"{folder}/style.css","w").write("body{background:black;color:white;text-align:center;}")
        open(f"{folder}/script.js","w").write("console.log('Website active');")

    elif project_type == "api":
        open(f"{folder}/api.py","w").write("from flask import Flask\napp=Flask(__name__)\n@app.route('/')\ndef home(): return 'API Running'")

    elif project_type == "dashboard":
        open(f"{folder}/dashboard.html","w").write("<html><body><h1>Dashboard Ready</h1></body></html>")

    elif project_type == "app":
        open(f"{folder}/main.py","w").write("print('App Generated')")
        open(f"{folder}/config.txt","w").write("configuration ready")

    return f"Builder created full {folder}"
