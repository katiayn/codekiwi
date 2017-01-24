import random
import string

from django.test import TestCase
import factory

from codekiwi.kiwitesting.models import Employee


def generate_random_str(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee

    last_name = factory.LazyAttribute(lambda t: generate_random_str())
    first_name = factory.LazyAttribute(lambda t: generate_random_str())
    job = factory.LazyAttribute(lambda t:generate_random_str(length=15))


class EmployeeTestCase(TestCase):

    def test_employee(self):
        # Generate a completely random saved employee instance
        # shortcut for EmployeeFactory.create()
        employee = EmployeeFactory()
        # Test assertions
        self.assertIsNotNone(employee.last_name)
        self.assertIsNotNone(employee.first_name)
        self.assertIsNotNone(employee.job)

    def test_another_employee(self):
        # Generate an employee with an explicit last_name
        employee = EmployeeFactory(last_name='Nakamura')
        # Test assertions
        self.assertTrue(employee.last_name, 'Nakamura')
        self.assertIsNotNone(employee.first_name)
        self.assertIsNotNone(employee.job)