import io
import sys

from person import Person

class TestPerson:
    def test_name_not_empty(self):
        '''prints "Name must be a string under 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string under 25 characters.\n"

    def test_name_string(self):
        '''prints "Name must be a string under 25 characters." if not a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name=123, job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string under 25 characters.\n"

    def test_name_length_over_25(self):
        '''prints "Name must be a string under 25 characters." if name length is over 25.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="This is a very long name that exceeds 25 characters", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string under 25 characters.\n"

    def test_valid_name(self):
        '''Does not print error message if name is valid.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="John Smith", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_valid_job(self):
        '''Does not print error message if job is valid.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Alice", job="Engineer")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_invalid_job(self):
        '''prints "Job must be in the list of approved jobs." if job is invalid.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Bob", job="Pilot")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Job must be in the list of approved jobs.\n"
