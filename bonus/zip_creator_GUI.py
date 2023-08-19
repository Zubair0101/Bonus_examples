import zip_creator
import PySimpleGUI as sg

sg.theme("DarkBrown2")

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")

choose_button1 = sg.FilesBrowse("Choose", key='files')
choose_button2 = sg.FolderBrowse("Location", key='folder')

input1 = sg.Input()
input2 = sg.Input()

compress_button = sg.Button("Compress")
output_label = sg.Text(key="Output")
Exit_button = sg.Button("Exit", tooltip='Exit the application.')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label],
                           [Exit_button]],
                   font=("Lucida sans", 14),
                   )

while True:
    event, values = window.read()
    print(event, values)
    try:
        filepaths = values["files"].split(';')
        folder = values["folder"]
    except (AttributeError, TypeError):
        break
    match event:
        case 'Compress':
            zip_creator.make_archive(filepaths, folder)
            window["Output"].update(value="Compression Completed!")

        case sg.WIN_CLOSED:
            break

        case "Exit":
            window.close()
            break
