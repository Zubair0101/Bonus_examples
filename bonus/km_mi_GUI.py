import PySimpleGUI as sg


def km_to_miles(km_) -> float:
    km_ = float(km_)
    return km_ / 1.6


sg.theme("SystemDefault")

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
convert_button = sg.Button("Convert")
Exit_button = sg.Button("Exit", key="Exit")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [convert_button, output], [Exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

        case "Exit":
            window.close()
            break
