FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Opens the file and returns the list of to-dos.
    :return: A list of data in string format.
    """
    with open(filepath, encoding='utf-8', newline='') as txt_file:
        task = txt_file.readlines()
    return task


def write_todos(task_arg: list, filepath=FILEPATH) -> None:
    """
    Writes the data in the text file.
    :param filepath: Path of the file to open.
    :param task_arg: The data to write to the file.
    :return: None
    """
    with open(filepath, 'w', encoding='utf-8', newline='') as txt_file:
        txt_file.writelines(task_arg)


# print(__name__)
# print(type(__name__))
# if __name__ == "__main__":
#     print("Hello from Functions.")

def count(phrase):
    return phrase.count('.')
