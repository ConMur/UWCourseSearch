from uwcoursesearch.services import uw_api_service

def test_getcoursecodes():
    codes = uw_api_service.get_course_codes()

    assert codes

def test_gettermcodes():
    codes, current_term = uw_api_service.get_term_codes()

    assert codes
    assert type(current_term) is int

    for code in codes:
        assert type(code.id) is int

def test_searchcourses():
    course_codes = uw_api_service.get_course_codes()
    term_codes, current_term = uw_api_service.get_term_codes()

    courses = uw_api_service.search_courses(current_term, "MATH", "136")

    assert type(courses) is not str

def test_searchcourses_badterm():
    error = uw_api_service.search_courses("2", "JAPAN", "101R")

    assert error == "No data returned"

def test_searchcourses_badcoursename():
    term_codes, current_term = uw_api_service.get_term_codes()
    error = uw_api_service.search_courses(current_term, "J", "101R")

    assert error == "No data returned"

def test_searchcourses_badcoursecode():
    course_codes = uw_api_service.get_course_codes()
    term_codes, current_term = uw_api_service.get_term_codes()

    error = uw_api_service.search_courses(current_term, course_codes[0],
    "-10")

    assert error == "No data returned"
