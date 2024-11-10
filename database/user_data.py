user_data = {}

def get_user_data(user_id):
    if user_id not in user_data:
        user_data[user_id] = {}
    return user_data[user_id]

def clear_user_data(user_id):
    if user_id in user_data:
        del user_data[user_id]

def set_echo_mode(user_id: int, mode: bool):
    user_data[user_id] = {"echo_mode": mode}

def is_echo_mode(user_id: int) -> bool:
    return user_data.get(user_id, {}).get("echo_mode", False)
