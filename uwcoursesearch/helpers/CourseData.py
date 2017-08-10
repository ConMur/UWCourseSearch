class CourseInfo:
    def __init__(self, course_code, text):
        self.code = course_code
        self.text = text

class TermInfo:
    """
    Represents a term.  Contains the id of the term (eg. 1179) and the name
    of the term (eg. Fall 2017)
    """
    def __init__(self, term_id, term_name):
        self.id = term_id
        self.name = term_name

class Reserves:
    def __init__(self, reserve_group, enrollment_capacity, enrollment_total):
        self.reserve_group = reserve_group
        self.enrollment_capacity = enrollment_capacity
        self.enrollment_total = enrollment_total

class Classes:
    def __init__(self, start_time, end_time, weekdays, start_date, end_date,
    is_tba, is_cancelled, is_closed, building, room, instructors):
        self.start_time = start_time
        self.end_time = end_time
        self.weekdays = weekdays
        self.start_date = start_date
        self.end_date = end_date
        self.is_tba = is_tba
        self.is_cancelled = is_cancelled
        self.is_closed = is_closed
        self.building = building
        self.room = room
        self.instructors = instructors

class Course:
    """
    Represents a course.  Contains the
    """

    def __init__(self, subject, catalog_number, units, title, note, class_number,
    section, campus, associated_class, related_component_1, related_component_2,
    enrollment_capacity, enrollment_total, topic, reserves, classes, held_with,
    term, academic_level, last_updated):
        self.subject = subject
        self.catalog_number = catalog_number
        self.units = units
        self.title = title
        self.note = note
        self.class_number = class_number
        self.section = section
        self.campus = campus
        self.associated_class = associated_class
        self.related_component_1 = related_component_1
        self.related_component_2 = related_component_2
        self.enrollment_capacity = enrollment_capacity
        self.enrollment_total = enrollment_total
        self.topic = topic
        self.classes = classes
        self.held_with = held_with
        self.term = term
        self.academic_level = academic_level
        self.last_updated = last_updated
