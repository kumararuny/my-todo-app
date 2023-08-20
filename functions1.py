
FILENAME = r'C:\Users\Arun\PycharmProjects\webapp1\todos.txt'

def get_todos():
    with open(FILENAME, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(towrite):
    with open(FILENAME, 'w') as file:
        file.writelines(towrite)










