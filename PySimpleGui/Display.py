import PySimpleGUI as sg
import openpyxl
import pandas as pd
from datetime import date
    
navset =[
    ['Go to',('Main', 
             'Basic Form', 
             'Student Form', 
             '---', 
             'Exit Form')]
]

layout = [
    [sg.Menu(navset)],
    [sg.Column([
        [sg.Text("Enter Name"), sg.InputText('', key='-INPUT-')],
        [sg.Button('Search', size=(10, 1))]
    ], justification='right', expand_x=True)],
    
     [sg.Text('Full Name', 
                 size=(15,1)), 
         sg.InputText(key='Full Name', 
                      size=30)
         ],
        
        [sg.Text('Address', 
                 size=(15,1)), 
         sg.InputText(key = 'Address', 
                      size=(30,3))
         ],
        
        [sg.Text('Age', 
                 size=(15,1)), 
         sg.InputText(key='Age', 
                      enable_events=True, 
                      size=7)
         ],
        
        [sg.Text('Gender', 
                 size=(15,1)), 
         sg.Combo(['Male', 'Female', 'LGBTQ'], 
                  key='Gender' )
         ],
        
        [sg.Text('Birthplace', 
                 size=(15,1)), 
         sg.InputText(key='Birthplace', 
                      size=30)
         ],
        
        [sg.Text('Birthdate', 
                 size=(15,1)), 
         sg.InputText(key='Birthdate', 
                      size=(10,1), 
                      enable_events=True), 
         sg.CalendarButton('', 
                           close_when_date_chosen=True, 
                           format='%m/%d/%y', 
                           image_filename='png/1.png')
         ],
        [sg.Multiline('', size=(90,20), no_scrollbar=True)]
]


window = sg.Window('Search and Update', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

window.close()