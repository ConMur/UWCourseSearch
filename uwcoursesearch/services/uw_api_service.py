import requests
from uwcoursesearch import app
from flask import flash
from uwcoursesearch.helpers.CourseData import Course, Classes, CourseInfo, Reserves, TermInfo


def get_course_codes():
    """
    Get a list of course codes and their definitions from the UW API
    """
    #Create the url to query the API with
    endpoint = """https://api.uwaterloo.ca/v2/codes/subjects.json?key={}\
    """.format(app.config['API_KEY'])

    #Query the API
    json = requests.get(endpoint).json()

    #Determine if there is an error
    error_message = _check_api_error_message(json)

    if(error_message is not ""):
        flash(error_message)
        abort(500)

    course_codes = []
    #Add course codes and their description to the dictionary
    for course in json['data']:
        course_code = course['subject']
        course_desc = course['description']

        text = "{} - {}".format(course_code, course_desc)

        course_object = CourseInfo(course_code, text)
        course_codes.append(course_object)

    return course_codes

def get_term_codes():
    """
    Get a list of term codes and their names from the UW API.  Returns a
    TermInfo object
    """

    #Create the url to query the API with
    endpoint = """https://api.uwaterloo.ca/v2/terms/list.json?key={}\
    """.format(app.config['API_KEY'])

    #Query the API
    json = requests.get(endpoint).json()

    #Determine if there is an error
    error_message = _check_api_error_message(json)

    if(error_message is not ""):
        flash(error_message)
        abort(500)

    term_codes = []
    #Add term codes and their names to the dictionary
    for year in json['data']['listings']:
        data = json['data']['listings'][year]
        for term in data:
            term_code = term['id']
            term_name = term['name']

            term_object = TermInfo(term_code, term_name)
            term_codes.append(term_object)

    return term_codes

def search_courses(term, course_name, course_code):
    """
    Searches for the specified course.  If there is an error while searching,
    returns an error message.  Otherwise, returns the courses matching the
    search criteria

    term -- the school term (eg. 1179)
    course_name -- the name of the course (eg. JAPAN)
    course_code -- the code number for the course (eg. 101R)
    """

    #Create the url to query the API with
    endpoint = """https://api.uwaterloo.ca/v2/terms/{}/{}/{}/schedule.json?key={}\
    """.format(term, course_name, course_code, app.config['API_KEY'])

    #Query the API
    json = requests.get(endpoint).json()

    #Determine if there is an error
    error_message = _check_api_error_message(json)

    if(error_message is not ""):
        return error_message

    data = []

    #Parse json response
    for course in json['data']:
        reserves_data = course['reserves']
        reserves = []
        for reserve in reserves_data:
            reserves.append(Reserves(reserve['reserve_group'],
                                reserve['enrollment_capacity'],
                                reserve['enrollment_total']))

        classes_data = course['classes']
        classes = []
        for class_ in classes_data:
            date_data = class_['date']
            location_data = class_['location']
            instructors_data = class_['instructors']

            classes.append(Classes(date_data['start_time'], date_data['end_time'],
            date_data['weekdays'], date_data['start_date'], date_data['end_date'],
            date_data['is_tba'], date_data['is_cancelled'], date_data['is_closed'],
            location_data['building'], location_data['room'], instructors_data))

        course_object = Course(course['subject'], course['catalog_number'], course['units'],
        course['title'], course['note'], course['class_number'],course['section'],
        course['campus'], course['associated_class'], course['related_component_1'],
        course['related_component_2'], course['enrollment_capacity'],
        course['enrollment_total'], course['topic'], reserves, classes,
        course['held_with'], course['term'], course['academic_level'],
        course['last_updated'])

        data.append(course_object)

    return data


def _check_api_error_message(json_data):
    """
    Returns an error if one occurred and an empty string if the response
    was successful

    json_data -- the data returned from the API query
    """
    #Ensure the response was received
    status_code = json_data['meta']['status']

    #Notify  if there are errors
    if status_code is not 200:
        error_message = json_data['meta']['message']
        return error_message

    return ""
