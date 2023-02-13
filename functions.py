import time
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_reader:
        todos_local = file_reader.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file_writer:
        file_writer.writelines(todos_arg)


def is_empty(todos_local):
    if len(todos_local) == 0:
        print("Todo list is empty.")


def print_todo(todos_local):
    for index, item in enumerate(todos_local):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)


def number(user_action):
    if user_action.startswith('edit'):
        actual_number_in_list = int(user_action[5:]) - 1
        return actual_number_in_list
    elif user_action.startswith("complete"):
        actual_number_in_list = int(user_action[9:]) - 1
        return actual_number_in_list


def get_time():
    return time.strftime("%b %d, %Y  %H:%M:%S")
