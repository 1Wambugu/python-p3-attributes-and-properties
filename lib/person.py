# person.py

APPROVED_JOBS = [
    "Engineer",
    "Teacher",
    "Doctor",
    "Sales",
    "Designer",
    "Manager",
    "Writer",
    "Chef",
]

class Person:
    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert name to title case
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
