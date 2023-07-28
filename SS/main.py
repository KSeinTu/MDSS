import PySimpleGUI as sg #pip install pysimplegui

# -- GUI Definition -- #

layout = [
    [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel Files", "*.xls*")))], # Input field to browse for a file, we also specify only browsing excel files
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()], # input field to browse for a folder
    [sg.Exit(),sg.Button("Convert to CSV")],
]

#key argument acts as the variable for out inputs

window = sg.Window("Excel 2 CSV Converter", layout)

while True:
    event, values = window.read()
    #print(event, values) # prints the keys to the command window
    if event in (sg.WINDOW_CLOSED, "Exit"): # This is the event of the exit buttton being closed or the x in the top right corner of the window
        break
    if event == "Convert to CSV": # if the user clicks the convert to CSV
        sg.popup_error("Not yet implmemented")
window.close()