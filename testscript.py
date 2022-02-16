from BCS_API_PCKG import bcs
# https://anaconda.org/conda-forge/python-dotenv
# !conda install -c conda-forge python-dotenv -y
from dotenv import load_dotenv
import os

load_dotenv()
bcs_username = os.getenv("BCS_USERNAME")
bcs_password = os.getenv("BCS_PASSWORD")

bcs_api_obj = bcs.BCS_API(bcs_username, bcs_password)
print(bcs_api_obj.headers)
print(bcs_api_obj.course_id)
print(bcs_api_obj.attendance)
print(bcs_api_obj.grades)
print(bcs_api_obj.bcs_weekly_feeback())