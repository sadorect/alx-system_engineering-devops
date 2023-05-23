#!/usr/bin/python3

import requests
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
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todos_data)

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{num_total_tasks}):")
    for task in completed_tasks:
        print("\t", task["title"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
