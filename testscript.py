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

# Add course_number arguement
bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)
print(bcs_api_obj.headers)
print(bcs_api_obj.course_id)
print(bcs_api_obj.attendance)
print(bcs_api_obj.grades)
print(bcs_api_obj.bcs_weekly_feeback())
