from BCS_API_PCKG import bcs
# https://anaconda.org/conda-forge/python-dotenv
# !conda install -c conda-forge python-dotenv -y
# from dotenv import load_dotenv
import dotenv
import os
import PySimpleGUI as sg

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Color_Names_Smaller_List.py
sg.theme('DarkGrey4')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your BCS Username, Password, & Course')],
    [sg.Text('Username (leave blank if completed before)', size=(35, 1)), sg.InputText()],
    [sg.Text('Password (leave blank if completed before)', size=(35, 1)), sg.InputText()],
    [sg.Text('Course [i.e. 0](leave blank if completed before)', size=(35, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()

# print(event, type(values[0]), values[1], values[2])  # the input data looks like a simple list when auto numbered

if values[0] != '':
    os.environ["BCS_USERNAME"] = values[0]
    dotenv.set_key(dotenv_file, "BCS_USERNAME", os.environ["BCS_USERNAME"])
if values[1] != '':
    os.environ["BCS_PASSWORD"] = values[1]
    dotenv.set_key(dotenv_file, "BCS_PASSWORD", os.environ["BCS_PASSWORD"])
if values[2] != '':
    os.environ["COURSE_NUMBER"] = values[2]
    dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
    
dotenv.load_dotenv()
bcs_username = os.getenv("BCS_USERNAME")
bcs_password = os.getenv("BCS_PASSWORD")
course_number = os.getenv("COURSE_NUMBER")

# MAKE TO ACCEPT course_number as arguement       
bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)

layout = [  [sg.Text('BCS Output')],
            [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(75,8))],
            [sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
            [sg.MLine(key='-ML3-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
            [sg.MLine(key='-ML4-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
            # [sg.MLine(key='-ML5-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
            # [sg.Button('Go'), sg.Button('Exit')]]
            [sg.Button('Exit')]]


window = sg.Window('Window Title', layout, finalize=True)


# Note, need to finalize the window above if want to do these prior to calling window.read()
window['-ML1-'+sg.WRITE_ONLY_KEY].print('AuthToken:\n', end='', font='Courier 12', text_color='red', background_color='yellow')
window['-ML1-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.headers,'\n',end='')
window['-ML1-'+sg.WRITE_ONLY_KEY].print('Course ID:\n', end='', font='Courier 12',text_color='white', background_color='green')
window['-ML1-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.course_id,end='')

window['-ML2-'+sg.WRITE_ONLY_KEY].print('Attendance:\n', end='', font='Courier 12',text_color='white', background_color='green')
window['-ML2-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.attendance,end='')

window['-ML3-'+sg.WRITE_ONLY_KEY].print('Grades:\n', end='', font='Courier 12',text_color='white', background_color='green')
window['-ML3-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.grades,end='')

window['-ML4-'+sg.WRITE_ONLY_KEY].print('Feedback\n', end='', font='Courier 12',text_color='white', background_color='green')
window['-ML4-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.bcs_weekly_feeback(),end='')

# counter = 0

while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # if event == 'Go':
    #     window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
    # window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
    # counter += 1
window.close()



# REFERENCE
# https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-1-shot-window-simple-data-entry-return-values-auto-numbered

# print = sg.Print

# sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)
# print('This is a normal print that has been re-routed.')

# Add course_number arguement
# bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)
# print(bcs_api_obj.headers)
# print(bcs_api_obj.course_id)
# print(bcs_api_obj.attendance)
# print(bcs_api_obj.grades)
# print(bcs_api_obj.bcs_weekly_feeback())


# sg.Print(bcs_api_obj.headers, text_color='white', background_color='green', font='Courier 10')
# sg.Print(bcs_api_obj.course_id)
# sg.Print(bcs_api_obj.attendance)
# sg.Print(bcs_api_obj.grades, background_color='red', text_color='white')
# sg.Print(bcs_api_obj.bcs_weekly_feeback(), bcs_api_obj.headers, 'such as sep', sep=',')
# sg.Print('To not extend a colored line use the "end" parm', background_color='blue', text_color='white', end='')
# sg.Print('\nThis line has no color.')


# layout = [  [sg.Text('What you print will display below:')],
#             [sg.Output(size=(50,10))],# key='-OUTPUT-')],
#             # [sg.In(key='-IN-')],
#             [sg.Button('Go'), sg.Button('Clear'), sg.Button('Exit')]  ]

# window = sg.Window('Window Title', layout)

# while True:             # Event Loop
#     event, values = window.read()
#     # print(event, values)
#     bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)
#     print(bcs_api_obj.headers)
#     print(bcs_api_obj.course_id)
#     print(bcs_api_obj.attendance)
#     print(bcs_api_obj.grades)
#     print(bcs_api_obj.bcs_weekly_feeback())
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     if event == 'Clear':
#         window['-OUTPUT-'].update('')
# window.close()



# layout = [[sg.VPush()],
#           [sg.Push(), sg.Text('Centered in the window'), sg.Push()],
#           [sg.Push(), sg.Button('Ok'), sg.Button('Cancel'), sg.Push()],
#           [sg.VPush()]]

# window = sg.Window('A Centered Layout', layout, resizable=True, size=(300, 300))

# while True:
#     event, values = window.read()
#     # bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)
#     print(bcs_api_obj.headers)
#     print(bcs_api_obj.course_id)
#     print(bcs_api_obj.attendance)
#     print(bcs_api_obj.grades)
#     print(bcs_api_obj.bcs_weekly_feeback())
#     if event in (sg.WIN_CLOSED, 'Cancel'):
#         break
# window.close()        