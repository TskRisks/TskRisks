import PySimpleGUI as sg
import pandas as pd
import BasicInformation
import Student
import sys

def create_window(theme): 
    sg.theme(theme)

    navset = [
        ['Option',[['Theme',[color]],
                   '---', 
                   'Exit']],   
    ]
    
    mainlayout = [
        [sg.Menu(navset, font=('Times',10))],
        [sg.Button('Basic Information', size=(10,5)), sg.Button('Student Information', size=(10,5))],
        [sg.Button('Form3', size=(10,5)), sg.Button('Form4',size=(10,5))]
    
    ]
    return sg.Window('Main Form', mainlayout, finalize=True)

color = [
        'DarkBlue', 'DarkBrown', 'DarkGreen', 'DarkGrey', 'DarkPurple',
        'DarkRed', 'DarkTeal', 'DarkAmber', 'DarkTanBlue', 'random'
    ]

window = create_window('DefaultNoMoreNagging')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        confirm_exit = sg.popup_ok_cancel('Are you sure you want to exit?', title='Confirm Exit?')
        if confirm_exit == 'OK':
            break
        elif confirm_exit == 'Cancel' or confirm_exit == sg.WINDOW_CLOSED:
            window.close()
            window = create_window(event)
            
    if event == 'Exit':
        confirm_exit1 = sg.popup_ok_cancel('Are you sure you want to exit?', title='Confirm Exit')
        if confirm_exit1 == 'OK':
            break
        elif confirm_exit1 == 'Cancel' or confirm_exit1 == sg.WIN_CLOSED:
            window.close()
            window = create_window(event)
             
            
    if event == 'Basic Information':
        window.hide()
        BasicInformation.fform(window)
        window.finalize()
        window.un_hide()
        
    if event == 'Student Information':
        window.hide()
        Student.student_form(window)
        window.finalize()
        window.un_hide()
    
    if event in color:
        window.close()
        window = create_window(event)       

window.close()
sys.exit
