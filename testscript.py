from BCS_API_PCKG import bcs
# https://anaconda.org/conda-forge/python-dotenv
# !conda install -c conda-forge python-dotenv -y
# from dotenv import load_dotenv
import dotenv
import os
import PySimpleGUI as sg

# dotenv_file = dotenv.find_dotenv()
# dotenv.load_dotenv(dotenv_file)

# # https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Color_Names_Smaller_List.py
# sg.theme('DarkGrey4')      # Add some color to the window

# # Very basic window.  Return values using auto numbered keys

# layout = [
#     [sg.Text('Please enter your BCS Username, Password, & Course')],
#     [sg.Text('Username (leave blank if completed before)', size=(35, 1)), sg.InputText()],
#     [sg.Text('Password (leave blank if completed before)', size=(35, 1)), sg.InputText()],
#     [sg.Text('Course [i.e. 0](leave blank if completed before)', size=(35, 1)), sg.InputText()],
#     [sg.Submit(), sg.Cancel()]
# ]

# window = sg.Window('Simple data entry window', layout)
# event, values = window.read()
# window.close()

# # print(event, type(values[0]), values[1], values[2])  # the input data looks like a simple list when auto numbered

# if values[0] != '':
#     os.environ["BCS_USERNAME"] = values[0]
#     dotenv.set_key(dotenv_file, "BCS_USERNAME", os.environ["BCS_USERNAME"])
# if values[1] != '':
#     os.environ["BCS_PASSWORD"] = values[1]
#     dotenv.set_key(dotenv_file, "BCS_PASSWORD", os.environ["BCS_PASSWORD"])
# if values[2] != '':
#     os.environ["COURSE_NUMBER"] = values[2]
#     dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
    
# dotenv.load_dotenv()
# bcs_username = os.getenv("BCS_USERNAME")
# bcs_password = os.getenv("BCS_PASSWORD")
# course_number = os.getenv("COURSE_NUMBER")

# # MAKE TO ACCEPT course_number as arguement       
# bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)

# layout = [  [sg.Text('BCS Output')],
#             [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(75,8))],
#             [sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
#             [sg.MLine(key='-ML3-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
#             [sg.MLine(key='-ML4-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
#             # [sg.MLine(key='-ML5-'+sg.WRITE_ONLY_KEY,  size=(75,8))],
#             # [sg.Button('Go'), sg.Button('Exit')]]
#             [sg.Button('Exit')]]


# window = sg.Window('Window Title', layout, finalize=True)


# # Note, need to finalize the window above if want to do these prior to calling window.read()
# window['-ML1-'+sg.WRITE_ONLY_KEY].print('AuthToken:\n', end='', font='Courier 12', text_color='red', background_color='yellow')
# window['-ML1-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.headers,'\n',end='')
# window['-ML1-'+sg.WRITE_ONLY_KEY].print('Course ID:\n', end='', font='Courier 12',text_color='white', background_color='green')
# window['-ML1-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.course_id,end='')

# window['-ML2-'+sg.WRITE_ONLY_KEY].print('Attendance:\n', end='', font='Courier 12',text_color='white', background_color='green')
# window['-ML2-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.attendance,end='')

# window['-ML3-'+sg.WRITE_ONLY_KEY].print('Grades:\n', end='', font='Courier 12',text_color='white', background_color='green')
# window['-ML3-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.grades,end='')

# window['-ML4-'+sg.WRITE_ONLY_KEY].print('Feedback\n', end='', font='Courier 12',text_color='white', background_color='green')
# window['-ML4-'+sg.WRITE_ONLY_KEY].print(bcs_api_obj.bcs_weekly_feeback(),end='')

# # counter = 0

# while True:             # Event Loop
#     event, values = window.read(timeout=100)
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     # if event == 'Go':
#     #     window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
#     # window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
#     # counter += 1
# window.close()

##################################################

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





"""
    Example of (almost) all Elements, that you can use in PySimpleGUI.
    Shows you the basics including:
        Naming convention for keys
        Menubar format
        Right click menu format
        Table format
        Running an async event loop
        Theming your application (requires a window restart)
        Displays the values dictionary entry for each element
        And more!

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg
from BCS_API_PCKG import bcs
# https://anaconda.org/conda-forge/python-dotenv
# !conda install -c conda-forge python-dotenv -y
# from dotenv import load_dotenv
import dotenv
import os
from pathlib import Path
import re


def make_window(theme):
# def make_window(theme, ):
    sg.theme(theme)
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']] ]
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing','More Nothing','Exit']]
    graph_right_click_menu_def = [[], ['Erase','Draw Line', 'Draw',['Circle', 'Rectangle', 'Image'], 'Exit']]

    input_layout =  [
                # [sg.Menu(menu_def, key='-MENU-')],
                [sg.Text('Please enter your BCS Username, Password, & Course (leave blank if completed before)', font='Helvetica 12')],
                [sg.Text('Username:'), sg.InputText(key='-USR-')],
                [sg.Text('Password:'), sg.InputText(key='-PSWRD-')],
                # [sg.Text('Course:', size=(35, 1)), sg.InputText()],
                [sg.Radio('Course0', "RadioDemo", default=True, size=(10,1), k='-R0-'), sg.Radio('Course1', "RadioDemo", default=False, size=(10,1), k='-R1-'), sg.Radio('Course2', "RadioDemo", default=False, size=(10,1), k='-R2-'), sg.Radio('Course3', "RadioDemo", default=False, size=(10,1), k='-R3-'), sg.Radio('Course4', "RadioDemo", default=False, size=(10,1), k='-R4-')],
        
#                 [sg.Slider(orientation='h', key='-SKIDER-'),
#                  sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'),],
#                 [sg.Checkbox('Checkbox', default=True, k='-CB-')],
                
#                 [sg.Combo(values=('Combo 1', 'Combo 2', 'Combo 3'), default_value='Combo 1', readonly=True, k='-COMBO-'),
#                  sg.OptionMenu(values=('Option 1', 'Option 2', 'Option 3'),  k='-OPTION MENU-'),],
                # [sg.Spin([i for i in range(1,11)], initial_value=10, k='-SPIN-'), sg.Text('Spin')],
#                 [sg.Multiline('Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.', size=(45,5), expand_x=True, expand_y=True, k='-MLINE-')],
                # [sg.Button('Confirm Login Info'), sg.Button('Popup'), sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-')]]
                [sg.Button('Confirm Login Info'), sg.Button('Popup')]]

    asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
               [sg.Image(data=sg.DEFAULT_BASE64_ICON,  k='-IMAGE-')],
               [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'), sg.Button('Test Progress bar')]]

    logging_layout = [[sg.Text("Use this for debugging.")],
                      [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                      ]
    
    # Table Data
    data = []
    heading = ['sessionName', 'studentName', 'pending', 'present', 'remote', 'excused']
    # heading = []
    
    students_data = []
    student_heading = ['    Students    ']
    
    # graphing_layout = [[sg.Text("Anything you would use to graph will display here!")],
                      # [sg.Graph((200,200), (0,0),(200,200),background_color="black", key='-GRAPH-', enable_events=True,
                      #           right_click_menu=graph_right_click_menu_def)],
                      # [sg.T('Click anywhere on graph to draw a circle')],
                      # [sg.Table(values=data, headings=headings, max_col_width=25,
    graphing_layout = [[sg.Table(values=students_data, 
                                headings=student_heading, 
                                max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                display_row_numbers=False,
                                justification='right',
                                # num_rows=2,
                                alternating_row_color='black',
                                key='-STUDENTTABLE-', 
                                # enable_events=True, # ADDED
                                row_height=25)],
                      [sg.Button('Update Students')],
                              [sg.Table(values=data, 
                                headings=heading, 
                                max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                display_row_numbers=True,
                                justification='right',
                                # num_rows=2,
                                alternating_row_color='black',
                                key='-TABLE-', 
                                # enable_events=True, # ADDED
                                row_height=25)],
                      [sg.Button('Update Table')]]

    
    # Table Data    
    grade_students_data = []
    grade_student_heading = ['    Students    ']
    
    assignments_data = []
    assignments_heading = ['       Assignments       ']    
    
    grade_data = []
    grade_heading = ['assignmentTitle', '   studentName   ', 'submitted', 'grade']
    
    
    grades_graphing_layout = [[sg.Table(values=grade_students_data, 
                                headings=grade_student_heading, 
                                max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                display_row_numbers=False,
                                justification='right',
                                # num_rows=2,
                                alternating_row_color='black',
                                key='-STUDENTGRADETABLE-', 
                                # enable_events=True, # ADDED
                                row_height=25), sg.Table(values=assignments_data, 
                                headings=assignments_heading, 
                                max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                display_row_numbers=False,
                                justification='right',
                                # num_rows=2,
                                alternating_row_color='black',
                                key='-ASSIGNMENTSTABLE-', 
                                # enable_events=True, # ADDED
                                row_height=25)],        
                      [sg.Button('Update G.Students'), sg.Button('Update Assignments')],
                              
                        
                              [sg.Table(values=grade_data, 
                                headings=grade_heading, 
                                max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                display_row_numbers=True,
                                justification='right',
                                # num_rows=2,
                                alternating_row_color='black',
                                key='-GRADETABLE-', 
                                # enable_events=True, # ADDED
                                row_height=25)],
                      [sg.Button('Update Grades Table')]]
    
    
#     popup_layout = [[sg.Text("Popup Testing")],
#                     [sg.Button("Open Folder")],
#                     [sg.Button("Open File")]]
    
#     theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
#                     [sg.Listbox(values = sg.theme_list(), 
#                       size =(20, 12), 
#                       key ='-THEME LISTBOX-',
#                       enable_events = True)],
#                       [sg.Button("Set Theme")]]
    
    layout = [ [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
                [sg.Text('Update All Button', size=(38, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout +=[[sg.TabGroup([[  sg.Tab('Login Info', input_layout),
                               # sg.Tab('Asthetic Elements', asthetic_layout),
                               sg.Tab('Attendance', graphing_layout),
                               sg.Tab('Grades', grades_graphing_layout),
                               # sg.Tab('Popups', popup_layout),
                               # sg.Tab('Theming', theme_layout),
                               sg.Tab('Log', logging_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),

               ]]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('BCS API INFO', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True,
                       # scaling=2.0,
                      return_keyboard_events=True 
                      )
    window.set_min_size(window.size)
    return window

def main():
    window = make_window(sg.theme())
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        # keep an animation running so show things are happening
        # window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            
            
            dotenv_file = dotenv.find_dotenv()
            dotenv.load_dotenv(dotenv_file)

            if values['-USR-'] != '':
                os.environ["BCS_USERNAME"] = values['-USR-']
                dotenv.set_key(dotenv_file, "BCS_USERNAME", os.environ["BCS_USERNAME"])
            if values['-PSWRD-'] != '':
                os.environ["BCS_PASSWORD"] = values['-PSWRD-']
                dotenv.set_key(dotenv_file, "BCS_PASSWORD", os.environ["BCS_PASSWORD"])
            if values['-R0-'] == True:
                os.environ["COURSE_NUMBER"] = '0'
                dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
            elif values['-R1-'] == True:
                os.environ["COURSE_NUMBER"] = '1'
                dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
            elif values['-R2-'] == True:
                os.environ["COURSE_NUMBER"] = '2'
                dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
            elif values['-R3-'] == True:
                os.environ["COURSE_NUMBER"] = '3'
                dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])
            elif values['-R4-'] == True:
                os.environ["COURSE_NUMBER"] = '4'
                dotenv.set_key(dotenv_file, "COURSE_NUMBER", os.environ["COURSE_NUMBER"])

            dotenv.load_dotenv()
            bcs_username = os.getenv("BCS_USERNAME")
            bcs_password = os.getenv("BCS_PASSWORD")
            course_number = os.getenv("COURSE_NUMBER")
                   
            bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password, course_number)
            
            # Update Student Table
            students_data = [[x] for x in bcs_api_obj.attendance.studentName.unique().tolist()]
            window['-STUDENTTABLE-'].update(students_data)
            
            # Update Attendance Table
            csv_dataset = Path(str(Path.cwd()) + '/' + 'data' + '/' + 'attendance.csv')
            bcs_api_obj.attendance.to_csv(csv_dataset, index=False)

            ATDATA = []
            with open(csv_dataset, "r") as txt_file:
                ATHEAD = txt_file.readline().replace('\n','').split(',')

                for line in txt_file:
                    ATDATA.append(line.replace('\n','').split(','))

            data = ATDATA
            window['-TABLE-'].update(data)
            
            # Update Grade Student Table
            grade_students_data = [[x] for x in bcs_api_obj.grades.studentName.unique().tolist()]
            window['-STUDENTGRADETABLE-'].update(grade_students_data.sort())
            
            # Update Grade Table
            csv_dataset_grades = Path(str(Path.cwd()) + '/' + 'data' + '/' + 'grades.csv')
            bcs_api_obj.grades.to_csv(csv_dataset_grades, index=False)

            GRDATA = []
            with open(csv_dataset_grades, "r") as txt_file:
                AGRHEAD = txt_file.readline().replace('\n','').split(',')    
                for line in txt_file:
                    GRDATA.append(line.replace('\n','').split(','))

            grade_data = GRDATA
            window['-GRADETABLE-'].update(grade_data)
            
            # Update Assignments Table
            assignments_data = bcs_api_obj.grades.assignmentTitle.unique().tolist()
            def atoi(text):
                return int(text) if text.isdigit() else text

            def natural_keys(text):
                '''
                alist.sort(key=natural_keys) sorts in human order
                http://nedbatchelder.com/blog/200712/human_sorting.html
                (See Toothy's implementation in the comments)
                '''
                return [ atoi(c) for c in re.split(r'(\d+)', text) ]

            assignments_data.sort(key=natural_keys)
            assignments_data = [[x] for x in assignments_data]
            window['-ASSIGNMENTSTABLE-'].update(assignments_data)
            
            
            
            
            # values.update({'-ATHEAD-': ATHEAD})
            # values.update({'-ATDATA-': ATDATA})
            # values.update({'-ATHEAD-': bcs_api_obj.attendance.columns.tolist()})
            
            
            # print(bcs_api_obj.headers)
            # print(bcs_api_obj.course_id)
            # print(bcs_api_obj.attendance)
            # print(bcs_api_obj.grades)
            # print(bcs_api_obj.bcs_weekly_feeback())

            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ',values[key])
            
            # GET SELECTED CELL VALUE
            # cell_index = [int(x) for x in values['-STUDENTGRADETABLE-']] 
            cell_index = 0
            for x in values['-STUDENTGRADETABLE-']:
                cell_index = x
            
            # cell_index = values['-STUDENTGRADETABLE-']
            print(cell_index)
            print(type(cell_index))
            print(students_data[cell_index])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        
        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup('BCS API Demo',
                     'Right click anywhere to see right click menu',
                     'Visit each of the tabs to see available elements',
                     'Output of event and values can be see in Output tab',
                     'Visit for additional info visit https://github.com/mcharipar/Bootcampspot_api.', keep_on_top=True)
        
        elif event == 'Popup':
            print("[LOG] Clicked Popup Button!")
            sg.popup("You pressed a button!", keep_on_top=True)
            print("[LOG] Dismissing Popup!")
        
        elif event == 'Test Progress bar':
            print("[LOG] Clicked Test Progress Bar!")
            progress_bar = window['-PROGRESS BAR-']
            for i in range(100):
                print("[LOG] Updating progress bar by 1 step ("+str(i)+")")
                progress_bar.update(current_count=i + 1)
            print("[LOG] Progress bar complete!")
        
        # elif event == "-GRAPH-":
        #     graph = window['-GRAPH-']       # type: sg.Graph
        #     graph.draw_circle(values['-GRAPH-'], fill_color='yellow', radius=20)
        #     print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
        
        
        # ADDED
        elif event == "Update Table":
            csv_dataset = Path(str(Path.cwd()) + '/' + 'data' + '/' + 'attendance.csv')
            bcs_api_obj.attendance.to_csv(csv_dataset, index=False)

            ATDATA = []
            with open(csv_dataset, "r") as txt_file:
                ATHEAD = txt_file.readline().replace('\n','').split(',')

                for line in txt_file:
                    ATDATA.append(line.replace('\n','').split(','))

            # heading = [[x] for x in bcs_api_obj.attendance.columns.tolist()]
            # heading = [[x] for x in ATHEAD]
            data = ATDATA
            
            # window['-TABLE-'].update(heading)
            window['-TABLE-'].update(data)
            # window.refresh()

            
        elif event == 'Update Students':
            students_data = [[x] for x in bcs_api_obj.attendance.studentName.unique().tolist()]
            try:
                # students_data
                window['-STUDENTTABLE-'].update(students_data)
            except:
                print('student update failed')
                
        elif event == "'Update G.Students'":
            csv_dataset_grades = Path(str(Path.cwd()) + '/' + 'data' + '/' + 'grades.csv')
            bcs_api_obj.grades.to_csv(csv_dataset_grades, index=False)

            GRDATA = []
            with open(csv_dataset_grades, "r") as txt_file:
                AGRHEAD = txt_file.readline().replace('\n','').split(',')    
                for line in txt_file:
                    GRDATA.append(line.replace('\n','').split(','))

            grade_data = GRDATA
            window['-GRADETABLE-'].update(grade_data)
            
        elif event == 'Update G.Students':
            grade_students_data = [[x] for x in bcs_api_obj.grades.studentName.unique().tolist()]
            try:
                # students_data
                window['-STUDENTGRADETABLE-'].update(grade_students_data)
            except:
                print('g.student update failed')
    
        elif event == 'Update Assignments':
            # Update Assignments Table
            assignments_data = bcs_api_obj.grades.assignmentTitle.unique().tolist()
            def atoi(text):
                return int(text) if text.isdigit() else text

            def natural_keys(text):
                '''
                alist.sort(key=natural_keys) sorts in human order
                http://nedbatchelder.com/blog/200712/human_sorting.html
                (See Toothy's implementation in the comments)
                '''
                return [ atoi(c) for c in re.split(r'(\d+)', text) ]

            assignments_data.sort(key=natural_keys)
            assignments_data = [[x] for x in assignments_data]
            try:
                window['-ASSIGNMENTSTABLE-'].update(assignments_data)
            except:
                print('Assignments update failed')
        
        
        
            
        elif event == "Open Folder":
            print("[LOG] Clicked Open Folder!")
            folder_or_file = sg.popup_get_folder('Choose your folder', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose folder: " + str(folder_or_file))
        elif event == "Open File":
            print("[LOG] Clicked Open File!")
            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose file: " + str(folder_or_file))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Versions':
            sg.popup(sg.get_versions(), keep_on_top=True)

    window.close()
    exit(0)

if __name__ == '__main__':
    sg.theme('black')
    sg.theme('dark red')
    sg.theme('dark green 7')
    # sg.theme('DefaultNoMoreNagging')
    main()