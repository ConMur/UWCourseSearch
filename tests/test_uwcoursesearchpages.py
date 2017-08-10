from uwcoursesearch import app
import pytest

@pytest.fixture
def test_app():
    app.testing = True
    return app.test_client()

def test_homepage(test_app):
    rv = test_app.get('/')

    assert b"UWCourseSearch" in rv.data

def test_searchpage(test_app):
    rv = test_app.get('/search')

    assert b"Search" in rv.data

def test_resultspage(test_app):
    rv = test_app.post('/results', data=dict(CourseCode='101r', CourseName='JAPAN',
    Term='1179'))

    assert b"Class" in rv.data and b"Section" in rv.data and b"Capacity" in rv.data \
    and b"Enrolled" in rv.data
