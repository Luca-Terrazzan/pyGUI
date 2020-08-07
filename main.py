import sys, os
import PySimpleGUI as sg

if len(sys.argv) == 1:
    folder = sg.popup_get_folder('Select a folder')
else:
    folder = sys.argv[1]

if not folder or not os.path.exists(folder):
    sg.popup("Invalid or non existing folder!")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', folder)