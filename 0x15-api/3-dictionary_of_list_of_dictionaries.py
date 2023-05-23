#!/usr/bin/python3

import requests
import json

def export_todo_all_employees():
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    # Retrieve all users
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Retrieve all todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare TODO list data in JSON format
    json_data = {}
    for user in users_data:
        user_id = user["id"]
        username = user["name"]
        user_todos = [task for task in todos_data if task["userId"] == user_id]
        json_data[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in user_todos
        ]

    # Export TODO list data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)

    print(f"TODO list data for all employees exported to {filename}.")

if __name__ == "__main__":
    export_todo_all_employees()
