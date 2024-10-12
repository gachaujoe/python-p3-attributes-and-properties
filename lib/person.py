#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# class Person:
#     pass

# lib/person.py

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", 
                     "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="Unknown", job="Admin"):
        self.name = name
        self.job = job

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    # Property for name
    name = property(get_name, set_name)

    # Getter for job
    def get_job(self):
        return self._job

    # Setter for job
    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    # Property for job
    job = property(get_job, set_job)
