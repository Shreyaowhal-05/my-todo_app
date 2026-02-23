FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todo_local = file.readlines()
    return todo_local


def write_todo(todos_arg,filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
