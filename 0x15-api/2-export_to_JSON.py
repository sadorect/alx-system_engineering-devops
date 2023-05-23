#!/usr/bin/python3

import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Retrieve employee information
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Retrieve employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todos_data)

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{num_total_tasks}):")
    for task in completed_tasks:
        print("\t", task["title"])

    # Prepare TODO list data in JSON format
    json_data = {
        "USER_ID": [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in todos_data
        ]
    }

    # Export TODO list data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)

    print(f"TODO list data exported to {filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
