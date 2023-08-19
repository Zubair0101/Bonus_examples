import functions as fn
import time

while True:
    now = time.strftime("%b %d, %Y  -  %H:%M:%S")
    print("It is ", now)
    user_action = input("Type add, show, edit, remove or quit: ").strip()
    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + '\n'

        tasks = fn.get_todos()

        tasks.append(todo)

        fn.write_todos(tasks)

    elif user_action.startswith("show"):
        print()
        tasks = fn.get_todos()

        # new_todos = [item.strip('\n') for item in tasks]    # list comprehension
        # for index, items in enumerate(new_todos):

        for index, items in enumerate(tasks):
            print(f"{index + 1}. {items.strip()}")
        print()
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            tasks = fn.get_todos()

            new_todo = input("Enter the new todo: ").capitalize()
            tasks[number] = new_todo + '\n'

            fn.write_todos(tasks)

        except ValueError:
            print("Your command is not a valid (try entering the number of the todo ;) ).")
            continue

    elif user_action.startswith("remove"):
        done = '-'
        try:
            tasks = fn.get_todos()

            done = int(user_action[6:]) - 1

            todo_to_remove = tasks[done].strip()

            tasks.pop(done)

            print(f"Todo '{todo_to_remove}' was removed from the list.")

            fn.write_todos(tasks)

        except IndexError:
            print(f"There is no item with {done + 1} index.")
    elif user_action.startswith("quit"):
        break
    else:
        print("Invalid Command!")

print("BYE!!")
