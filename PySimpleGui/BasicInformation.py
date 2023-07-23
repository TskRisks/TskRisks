import PySimpleGUI as sg
import pandas as pd
import Student
import sys
from datetime import date 

def fform(main_window):
    
    navset = [
        ['Go to', ['Main', 'Student Form', '---', 'Exit Form']]
    ]
    
    EXCEL_FILE = 'Form Data/BasicForm.xlsx'
    try:
        
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame()
    
    layout = [
        [sg.Menu(navset)],
        [sg.Text('Basic Information Form', 
                 font='Franklin 18' , 
                 justification='center', 
                 expand_x=True, 
                 pad=(10,20))
         ],
        
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
        
        [sg.Submit()]
    ]

    window = sg.Window('Simple Form', layout)

    while True:
        event, values = window.read()
        if event == 'Exit Form':
            sg.popup_ok('You will go back to main', title='Reminder!')
            break
        
        if event == sg.WIN_CLOSED:
            exit_program = sg.popup_ok_cancel('Are you sure you want to Close the Program?', title='Caution!')
            if exit_program == 'OK':
                sg.popup('Thank you for using the program.', title='Thank you')
                window.close()
                sys.exit(0)
            elif exit_program == 'Cancel' or exit_program == sg.WIN_CLOSED:
                window.close()
                window = fform(main_window)
                
        if event == 'Main':
            window.close()
            break
        
        if event == 'Student Form':
            window.close()
            Student.student_form(window)
            break
        
        
            
        if event == 'Submit':
            
            if any(value == '' for value in values.items() if value != values['Birthdate']):
                sg.popup('Fill the necessary field.')
            else:
                age = values['Age']
                if not age.isdigit():
                    sg.popup('Age must be a number.')
                else:
                    newrecord = pd.DataFrame(values, index=[0])
                    df = pd.concat([df, newrecord], ignore_index=False)
                    df.to_excel(EXCEL_FILE, index=False)
                    sg.popup('Data Saved')
                    window['Full Name']('')
                    window['Address']('')
                    window['Age']('')
                    window['Gender']('')
                    window['Birthplace']('')
                    window['Birthdate']('')
        if event == 'Open':
            selected_date = sg.popup_get_date()
            if selected_date is not None:
                window['Birthdate'].update(selected_date.strftime('%m/%d/%y'))

    window.close()

if __name__ == '__main__':
    fform(None)
