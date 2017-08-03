import requests


def get_course_codes(api_key):
    """
    Get a list of course codes and their definitions from the UW API

    api_key -- the key to access the API
    """
    #Create the url to query the API with
    endpoint = """https://api.uwaterloo.ca/v2/codes/subjects.json?key={}\
    """.format(api_key)

    #Query the API
    json = requests.get(endpoint).json()

    _ensure_good_API_response(json)

    course_codes = []
    #Add course codes and their description to the dictionary
    for course in json['data']:
        course_code = course['subject']
        course_desc = course['description']
        text = "{} - {}".format(course_code, course_desc)
        course_codes.append(text)

    return course_codes

def get_term_codes(api_key):
    """
    Get a list of term codes and their names from the UW API.  Returns a
    Term object

    api_key -- the key to access the API
    """

    #Create the url to query the API with
    endpoint = """https://api.uwaterloo.ca/v2/terms/list.json?key={}\
    """.format(api_key)

    #Query the API
    json = requests.get(endpoint).json()

    _ensure_good_API_response(json)

    term_codes = []
    #Add term codes and their names to the dictionary
    for year in json['data']['listings']:
        data = json['data']['listings'][year]
        for term in data:
            term_code = term['id']
            term_name = term['name']

            term_object = Term(term_code, term_name)
            term_codes.append(term_object)

    return term_codes

class Term:
    """
    Represents a term.  Contains the id of the term (eg. 1179) and the name
    of the term (eg. Fall 2017)
    """
    def __init__(self, term_id, term_name):
        self.id = term_id
        self.name = term_name

def _ensure_good_API_response(json_data):
    """
    If the response code from the API is not 200, aborts the program with a
    500 error

    json_data -- the data returned from the API query
    """
    #Ensure the response was received
    status_code = json_data['meta']['status']

    #Notify  if there are errors
    if status_code is not 200:
        error_message = json_data['meta']['message']
        print("Error getting course code data: {}".format(error_message))
        abort(500)
