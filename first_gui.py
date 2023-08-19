import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")
clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")

# Input box and output box
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
output = sg.Text(key='output', text_color='lime')

list_box = sg.Listbox(values=functions.get_todos(),
                      key='existing_todos',
                      enable_events=True,
                      size=(45, 10))
# The buttons in th GUI
# Add_button = sg.Button("Add", tooltip='Adds the to-do in the list') # size=10)
Add_button = sg.Button(key="Add", tooltip='Adds the to-do in the list', image_size=(40, 30), image_source="add.png")
Edit_button = sg.Button("Edit", key="Edit",
                        tooltip='Edit the to-do in the list', )  # image_size = (40, 30), image_source = "edit.png")
Remove_button = sg.Button(key="Remove", tooltip='Removes the to-do from list', image_size=(40, 30),
                          image_source="complete.png")
Exit_button = sg.Button("Exit", tooltip='Exit the application.', )

layout = [[clock],
          [label],
          [input_box, Add_button],
          [list_box, Edit_button, Remove_button],
          [Exit_button, output]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Comic sans ms', 15))  # font=('Ink Free', 16))
# 'LAYOUT=' --> both objects placed in one list aligns them on 1 line

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y : %H - %M - %S"))
    # print(event)
    # print(values)
    # print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')
            functions.write_todos(todos)

            list_box.update(values=todos)
            window['output'].update(value="To-do added.", text_color="lime")
            # sg.popup("To-do added!")
        case "Edit":
            try:
                todo_to_edit = values['existing_todos'][0]  # To only get the string
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)  # To get the index of the todo_to_edit
                todos[index] = new_todo
                functions.write_todos(todos)

                window['existing_todos'].update(values=todos)
            except IndexError:
                # window['output'].update(value="Select a to-do to edit!", text_color="red")
                sg.popup("Select a to-do to edit!", font=("Comic sans ms", 16))
        # When clicking on a to-do, the said to-do appears in the text/input-box.
        case 'existing_todos':
            window['todo'].update(value=values['existing_todos'][0])

        case 'Remove':
            try:
                todos = functions.get_todos()
                todo_to_remove = values['existing_todos'][0]
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['existing_todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                # window['output'].update(value="Select a to-do to remove!", text_color="red")
                sg.popup("Select a to-do to remove!", font=("Comic sans ms", 16))

        case sg.WIN_CLOSED:
            break

        case 'Exit':
            break

window.close()
