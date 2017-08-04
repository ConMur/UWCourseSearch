from flask import render_template, url_for, request
from uwcoursesearch import app
from uwcoursesearch.services import uw_api_service

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    term_codes = uw_api_service.get_term_codes()
    course_codes = uw_api_service.get_course_codes()

    return render_template("search.html", term_codes=term_codes,
                            course_codes=course_codes)

@app.route('/results', methods=['POST'])
def results():
    term = request.form['Term']
    course_name = request.form['CourseName']
    course_code = request.form['CourseCode']

    data = uw_api_service.search_courses(term, course_name, course_code)

    if(type(data) is str):
        return render_template("results-badsearch.html", error=data)
    else:
        return render_template("results.html", data=data)
