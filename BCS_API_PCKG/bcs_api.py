"""
A collection of classes to simplify connecting the the bootcampspot.com api.

.. warning::

   This is an experimental package and subject to breaking changes
   without warning.
"""

import requests
import pandas as pd

class BCS_API:
    """Class that accepts BCS User Login (email address)
        and Password. https://bootcampspot.com/"""
    
    import requests
    import pandas as pd
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

        url = 'https://bootcampspot.com/api/instructor/v1/login'
        data = {
        "email": "{}".format(self.username),
        "password": "{}".format(self.password)}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        response_json = response_json['authenticationInfo']
        # df = pd.DataFrame(response_json, index=range(0,index))
        df = pd.DataFrame(response_json, index=range(0,1))
        # return df

        # def authToken():
        """Accepts DF from `bcs_login` and returns dictionary header to be used with requests module."""
        col_list = []
        for x in df.columns:
            col_list.append(x)
        col_list = col_list[-1]
        # input_df['authToken']
        token = '\'{}\': \'{}\''.format(col_list, response_json['authToken'])
        content_header = '"Content-Type": "application/json; charset=utf-8"'
        headers = "{{{}, {}}}".format(content_header, token)
        headers = eval(headers)
        self.headers = headers
        # return headers

        

#     def bcs_login(username, password):
#         """Returns `authToken` and header for . Accpets BCS User Login (email address)
#         and Password. https://bootcampspot.com/"""
#         import pandas as pd

#         url = 'https://bootcampspot.com/api/instructor/v1/login'
#         data = {
#         "email": "{}".format(username),
#         "password": "{}".format(password)}
#         headers = {"Content-Type": "application/json; charset=utf-8"}
#         response = requests.post(url, headers=headers, json=data)
#         response_json = response.json()
#         response_json = response_json['authenticationInfo']
#         # df = pd.DataFrame(response_json, index=range(0,index))
#         df = pd.DataFrame(response_json, index=range(0,1))
#         # return df

#         # def authToken():
#         """Accepts DF from `bcs_login` and returns dictionary header to be used with requests module."""
#         col_list = []
#         for x in df.columns:
#             col_list.append(x)
#         col_list = col_list[-1]
#         # input_df['authToken']
#         token = '\'{}\': \'{}\''.format(col_list, response_json['authToken'])
#         content_header = '"Content-Type": "application/json; charset=utf-8"'
#         headers = "{{{}, {}}}".format(content_header, token)
#         headers = eval(headers)
#         return headers

    # def me(input_header):
    def me(self):
        """Accepts dictionary header and returns Course ID info."""

        import pandas as pd

        url = 'https://bootcampspot.com/api/instructor/v1/me'
        # headers = input_header
        # response = requests.get(url, headers=headers)
        response = requests.get(url, headers=self.headers)

        response_json = response.json()
        # return response_json
        # RETURNS TUPLE IF MULTIPLE ACCOUNTS ASSOCIATED WITH USER
        try:
            self.course_id = eval(str(response_json['Enrollments']).strip('[]'))['courseId']
        except:
            self.course_id = eval(str(response_json['Enrollments'][0]).strip('[]'))['courseId']

    def bcs_attendance(self):
        """Accepts Course ID and dictionary header. Returns dataframe of students attendance for all sessions."""
        import pandas as pd

        url = 'https://bootcampspot.com/api/instructor/v1/attendance'
        data = {"courseId": self.course_id}
        headers = self.headers
        response = requests.post(url, headers=headers, json=data)

        response_json = response.json()
        return pd.DataFrame(response_json)

    def bcs_grades(self):
        """Accepts Course ID and dictionary header. Returns dataframe of students grades for all assignents."""
        import pandas as pd

        url = 'https://bootcampspot.com/api/instructor/v1/grades'
        data = {"courseId": input_course_id}
        headers = input_header
        response = requests.post(url, headers=headers, json=data)

        response_json = response.json()
        return pd.DataFrame(response_json)

    def bcs_weekly_feeback(input_course_id, input_header):
        """Accepts Course ID and dictionary header. Returns dataframe of students grades for all assignents."""
        import pandas as pd

        url = 'https://bootcampspot.com/api/instructor/v1/weeklyFeedback'
        data = {"courseId": input_course_id}
        headers = input_header
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        # return response_json

        my_dict = dict() 
        for index,value in enumerate(response_json['submissions']):
            my_dict[index] = value

        stud_feedback_df = pd.DataFrame()

        for x in my_dict:
            feedback_df = pd.DataFrame(my_dict[x])
            feedback_df.drop(['answers'], axis = 1, inplace = True)

            temp_df = pd.DataFrame()
            temp_df1 = pd.DataFrame()
            for y in my_dict[x]['answers']:
                try:
                    temp_df1 = pd.DataFrame(y)
                    # temp_df1 = pd.DataFrame(my_dict[0]['answers'][1])
                    temp_df = pd.concat([temp_df,temp_df1])
                except:
                    pass

            temp_df.reset_index(drop=True, inplace=True)
            stud_feedback_df1 = pd.concat([feedback_df, temp_df], axis=1)
            stud_feedback_df = pd.concat([stud_feedback_df, stud_feedback_df1])
        stud_feedback_df.index = stud_feedback_df['username']
        stud_feedback_df.drop(['username'], axis = 1, inplace = True)
        return stud_feedback_df