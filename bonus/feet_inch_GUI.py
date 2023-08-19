from bonus import bonus13
import PySimpleGUI as sg

sg.theme("Black")

feet_input = sg.InputText(key='feet')
inch_input = sg.InputText(key='inch')
output = sg.Text(key='output')

label1 = sg.Text("Enter feet: ")
label2 = sg.Text("Enter inches: ")

convert_button = sg.Button("Convert", key="Convert")
Exit_button = sg.Button("Exit", key="Exit")

window = sg.Window("Feet to meter converter",
                   layout=[[label1, feet_input], [label2, inch_input], [convert_button, output], [Exit_button]],
                   font=('Lucida sans', 16)
                   )

while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                meters = bonus13.convert(values['feet'], values['inch'])
                window['output'].update(value=meters, text_color='lime')
            except ValueError:
                window["output"].update(value="Please enter sufficient values.", text_color="red")
        case sg.WIN_CLOSED:
            break

        case "Exit":
            window.close()
            break
