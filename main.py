import PySimpleGUI as sg
from os import curdir
import os.path


CUR_PATH = ''
SEED = 716
CHOICES = ['choice1', 'choice2', 'choice3', 'choice4']
FONT = 'Courier 11'

# First the window layout in 2 columns
file_list_column = [
    [
        sg.Text("BG"),
        sg.In(size=(15, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(30, 50), key="-FILE LIST-"
        )  
    ],
]

file_list_column_2 = [
    [
        sg.Text("FG"),
        sg.In(size=(15, 1), enable_events=True, key="-FOLDER FG-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST FG-"
        )
    ],
]

style_selection_column = [
    [
        sg.Text("Choose style"),
    ],
    [
        # sg.Text("Choose style to be transferred"),
        sg.Listbox(
            values=['clear', 'autumn', 'cloudy', 'snowy', 'sunset', 'night'], enable_events=True, size=(10, 10), key="-DROP DOWN-"
        )
    ]
]

image_viewer_column = [
    # [sg.Text("Choose BG")],
    # [sg.Text(size=(25, 1), key="-TOUT-")],
    [sg.Text("", key="status", font=FONT, justification='center')],
    [sg.Image(key="-IMAGE-")],
    # [sg.Text("Context Based Object Placement done!")],
]

image_viewer_column_2 = [
    [sg.Text("Choose FG")],
    [sg.Text(size=(25, 1), key="-TOUTFG-")],
    [sg.Image(key="-IMAGEFG-")],
]

style_column = [
    [sg.Column(style_selection_column)],
    [sg.Text("No style", size=(10,1), key="style")],
]

instructions_column = [
    [sg.Text("Instructions", font=FONT)],
    [sg.Text("1. Instruction 1", font=FONT)],
    [sg.Text("2. Instruction 2", font=FONT)],
    [sg.Text("3. Instruction 3", font=FONT)],
    [sg.Text("4. Instruction 4", font=FONT)],
    [sg.Text("5. Instruction 5", font=FONT)],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeparator(),
        sg.Column(instructions_column),
       [sg.Button('METHOD 1'),
        sg.Combo(CHOICES, default_value=STYLES[0], key="style"),
        sg.Button('METHOD 2'),
        sg.Exit()],
    ]
]

window = sg.Window("Image Viewer", layout, size=(1100, 500))

while True:
    event, values = window.read()
    if event == "Exit" or event ==  sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg"))
        ]
        window["-FILE LIST-"].update(fnames)
    
    elif event == "-FILE LIST-": # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            img = Image.open(filename).resize((256, 256))
            new_filename = f'{filename[:-3]}png'
            img.save(new_filename)
            CUR_PATH = new_filename
            window["-IMAGE-"].update(filename=new_filename)
            window['status'].update("")
        except:
            pass
    
    elif event == "METHOD 1":
        # you can implement your method here
        pass

    elif event == "METHOD 2":
        # you can implement your method 2 here
        pass

window.close()