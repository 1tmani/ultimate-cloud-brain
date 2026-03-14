def deploy_status(target="render"):
    if target == "render":
        return "Deploy executor active: Render ready"
    return "Deploy executor active"
