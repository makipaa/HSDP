import config

def validate_user(username, password):
    if (username == config.DONOR["username"]) & (password == config.DONOR["password"]):
        return "donor"
    elif (username == config.DOCTOR["username"]) & (password == config.DOCTOR["password"]):
        return "doctor"
    else:
        return None