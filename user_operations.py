import requests


def get_user(id):
    response = requests.get(f"https://sdw-2023-prd.up.railway.app/users/{id}")
    return response.json() if response.status_code == 200 else None


def get_users(user_ids):
    users = [user for id in user_ids if (user := get_user(id)) is not None]
    return users


def update_user(user):
    response = requests.put(
        f"https://sdw-2023-prd.up.railway.app/users/{user['id']}", json=user
    )
    return True if response.status_code == 200 else False
