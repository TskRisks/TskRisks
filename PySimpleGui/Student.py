import PySimpleGUI as sg
import pandas as pd
import sys
import BasicInformation

def student_form(main_window):
    
    navset = [
        ['Go to',['Main','Basic Form','---', 'Exit Form']]
    ]
    
    EXCEL_FILE = 'StudentForm.xlsx'
    try:
        
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame()
    
    Student_layout = [
        [sg.Menu(navset)],
        [sg.Text('Student Form', 
                 font='Franklin 26', 
                 justification='center', 
                 expand_x=True, 
                 pad=(10, 20))
         ],
        [sg.Text('Name', 
                 size=(15,1)),
         sg.InputText(key='Full Name',
                      size=30,
                      enable_events=True)
         ],
        [sg.Text('Address', 
                 size=(15,1)),
         sg.InputText(key='Address',
                      size=(30,3))
         ],
        [sg.Text('Email', 
                 size=(15,1)),
         sg.InputText(key='Email',
                      size=30),
         sg.Text('Ex. abcd@gmail.com')
         ],
        [sg.Text('Mobile Number', 
                 size=(15,1)),
         sg.InputText( key='Mobile Number',
                      size=30),
         sg.Text(' Ex. 09123456789')
         ],
        [sg.Text('College/Univesity', 
                 size=(15,1)),
         sg.InputText(key='College',
                      size=30)
         ],
        [sg.Text('Course', 
                 size=(15,1)),
         sg.Combo(['Engineering', 'Computer Science', 'Information Technology',
                   'Accountancy', 'Chemist', 'Physicist', 'Economics', 'Psychology',
                   'Social Science', 'Political Science', 'Architecture',
                   'Philosopy', 'Sociology', 'Humanities', 'Mechanical Engineering',
                   'Chemical Engineering', 'Electrical Engineering', 'Statistics',
                   'Antropology', 'Education', 'Biochemistry', 'Communication arts','Other'],
                  key='Course',
                  size=30)
         ],
        [sg.Text('Gender', 
                 size=(15,1)),
         sg.Combo(['Male', 'Female', 'LGBTQ'],
                  key='Gender')
         ],
        [sg.Text('Citizenship', 
                 size=(15,1)),
         sg.InputText(key='Citizenship',
                      size=30)
         ],
        [sg.Text('Country of Origin', 
                 size=(15,1)),
         sg.Combo(['Philippines', 'Australia', 'Japan', 
                   'South Korea', 'Japan', 'China', 
                   'Singapore', 'India', 'Indonesia', 
                   'Vietnam', 'USA', 'France', 'Sweden', 
                   'Slovakia', 'Switzerland', 'Netherland', 
                   'Africa', 'Canada', 'New Zealand', 'Russia', 'Other'],
                  key='Country',
                  size=30)
         ],
        [sg.Text('Age', 
                 size=(15,1)),
         sg.InputText(key='Age',
                      size=30,
                      enable_events=True)
         ],
        [sg.Text('Birthplace', 
                 size=(15,1)),
         sg.InputText(key='Birthplace',
                      size=30)
         ],
        [sg.Text('Birthdate', 
                 size=(15,1)),
         sg.InputText(key='Birthdate',
                      size=30),
         sg.CalendarButton('', 
                           close_when_date_chosen=True, 
                           format='%m/%d/%y', 
                           image_filename='png/1.png')
         ],
        [sg.Text('------------------------------------------------------------Parents Information---------------------------------------------------------------------------'),
         ],
        [sg.Text('Mothers Name', 
                 size=(15,1)),
         sg.InputText(key='Mothers Name',
                      size=30)
        ],
         [sg.Text('Occupation', 
                 size=(15,1)),
         sg.InputText(key='Mothers Occupation',
                      size=30)
         ],
         [sg.Text('Mobile Number', 
                 size=(15,1)),
         sg.InputText(key='Mothers Mobile',
                      size=30),
         sg.Text(' Ex. 09123456789')
         ],
         [sg.Text('Fathers Name', 
                 size=(15,1)),
         sg.InputText(key='Fathers Name',
                      size=30)
        ],
         [sg.Text('Occupation', 
                 size=(15,1)),
         sg.InputText(key='Fathers Occupation',
                      size=30)
         ],
         [sg.Text('Mobile Number', 
                 size=(15,1)),
         sg.InputText(key='Fathers Mobile',
                      size=30),
         sg.Text(' Ex. 09123456789')
         ],
        
        [sg.Submit()]    
    ]
    
    window = sg.Window('Student Form', Student_layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit_program = sg.popup_ok_cancel('Are you sure you want to exit the program?', title='Caution!')
            if exit_program == 'OK':
                sg.popup('Thank you for using the program', title='Thank you')
                window.close()
                sys.exit(0)
            elif exit_program == 'Cancel' or exit_program == sg.WIN_CLOSED:
                window.close()
                window = student_form(main_window)
        
        if event == 'Exit Form':
            sg.popup_ok('You will go back to Main.', title='Okay')
            break
        
        if event == 'Main':
            window.close()
            break
        
        if event == 'Basic From':
            window.close()
            BasicInformation.fform(window)
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
                    window['Email']('')
                    window['Mobile Number']('')
                    window['College']('')
                    window['Course']('')
                    window['Gender']('')
                    window['Citizenship']('')
                    window['Country']('')
                    window['Age']('')
                    window['Birthplace']('')
                    window['Birthdate']('')
        if event == 'Open':
            selected_date = sg.popup_get_date()
            if selected_date is not None:
                window['Birthdate'].update(selected_date.strftime('%m/%d/%y'))
        
        
    window.close()
if __name__ == '__main__':
    student_form(None)
