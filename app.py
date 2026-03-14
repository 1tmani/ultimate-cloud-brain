from flask import Flask, request
from commands import execute
from memory import save_command
from ui_engine import page
from database import init_db, save_db

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    output = "System Active 🚀"
    if request.method == "POST":
        command = request.form["command"]
        save_command(command)
        save_db(command)
        output = execute(command)
    return page(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    cmd = data.get("command")

    if cmd == "/deploy-now":
        return jsonify({"result": "Deployment triggered"})

    elif cmd == "/fix-ui":
        return jsonify({"result": "UI repair module ready"})

    elif cmd == "/add-feature":
        return jsonify({"result": "Feature builder started"})

    return jsonify({"result": "Unknown command"})
