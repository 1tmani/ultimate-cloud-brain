from ai_core import decide
from builder import build_project
from deploy_engine import deploy_status
from repair import repair_command
from memory import load_history
from project_reader import read_project
from api_connector import api_status
from upgrade import upgrade_system
from automation_core import automate
from learning_engine import learn
from external_connector import external_status
from auth_engine import auth_status
from evolution_engine import evolve
from mutation_engine import mutate
from stability_engine import stabilize
from growth_engine import grow
from purpose_engine import mission

def think(command):
    priority = mission(command)
    command = repair_command(command.lower())

    if "build website" in command:
        build_project("website")
        return f"{priority} | " + automate("generated_website")

    if "build api" in command:
        build_project("api")
        return f"{priority} | " + automate("generated_api")

    if "build dashboard" in command:
        build_project("dashboard")
        return f"{priority} | " + automate("generated_dashboard")

    if "build app" in command:
        build_project("app")
        return f"{priority} | " + automate("generated_app")

    if "learn" in command:
        return f"{priority} | " + learn(command)

    if "external status" in command:
        return f"{priority} | " + external_status()

    if "auth status" in command:
        return f"{priority} | " + auth_status()

    if "evolve" in command:
        return f"{priority} | " + evolve()

    if "mutate" in command:
        return f"{priority} | " + mutate()

    if "stabilize" in command:
        return f"{priority} | " + stabilize()

    if "grow" in command:
        return f"{priority} | " + grow()

    if "read project" in command:
        return f"{priority} | " + read_project("generated_website")

    if "deploy render" in command:
        return f"{priority} | " + deploy_status("render")

    if "api status" in command:
        return f"{priority} | " + api_status()

    if "history" in command:
        return f"{priority} | " + str(load_history())

    if "upgrade" in command:
        return f"{priority} | " + upgrade_system()

    return f"{priority} | " + decide(command)
