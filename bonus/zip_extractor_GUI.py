import zip_extractor
import PySimpleGUI as sg

sg.theme("DarkBrown4")

label1 = sg.Text("Select Archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='file')

label2 = sg.Text("Select folder: ")
choose_button2 = sg.FolderBrowse("Location", key='folder')

input2 = sg.Input()
extract_button = sg.Button("Extract", key="Extract")
output_label = sg.Text(key="Output")    # , text_color="red")

Exit_button = sg.Button("Exit", tooltip='Exit the application.')

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label],
                           [Exit_button]],
                   font=("Lucida sans", 14),
                   )

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    archive_path = ''
    dest_folder = ''
    try:
        archive_path = values["file"]
        dest_folder = values["folder"]
    except TypeError:
        pass

    match event:
        case 'Extract':
            try:
                zip_extractor.extract_archive(archive_path, dest_folder)
                window["Output"].update(value="Extraction Completed!")
                # print(window['label1'])
            except FileNotFoundError:
                window["Output"].update(value="Select file to extract.")

        case sg.WIN_CLOSED:
            break

        case "Exit":
            window.close()
            break
