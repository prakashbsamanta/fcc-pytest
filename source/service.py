import requests

database = {
    1: "Alice",
    2: "Sam",
    3: "Danial"
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_json_placeholder_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
