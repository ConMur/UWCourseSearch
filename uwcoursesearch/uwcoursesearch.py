from flask import Flask, render_template, request, url_for

import os
import sys
from  uwcoursesearch.services import uw_api_service

app = Flask(__name__)

#Set up configuration
app.config.from_object('uwcoursesearch.config')
app.config['API_KEY'] = os.environ['API_KEY']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    api_key = app.config['API_KEY']

    css_url = url_for('static', filename="grid.css")

    term_codes = uw_api_service.get_term_codes(api_key)
    course_codes = uw_api_service.get_course_codes(api_key)

    return render_template("search.html", css_url=css_url, term_codes=term_codes,
                            course_codes=course_codes)

@app.route('/results', methods=['POST'])
def results():
    term = request.form['Term']
    course_name = request.form['CourseName']
    course_code = request.form['CourseCode']
    if(valid_search_terms(term, course_name, course_code)):
        data = search_courses(term, course_name, course_code)
        return render_template("results.html", data=data)
    else:
        return render_template("results-badsearch.html")
