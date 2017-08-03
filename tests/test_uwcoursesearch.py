from uwcoursesearch import app
import pytest

@pytest.fixture
def test_app():
    app.testing = True
    return app.test_client()

def test_homepage(test_app):
    rv = test_app.get('/')

    assert b"UWCourseSearch" in rv.data
