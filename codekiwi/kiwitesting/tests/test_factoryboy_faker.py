from django.test import TestCase
import factory

from codekiwi.kiwitesting.models import Employee


class EmployeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Employee

    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    job = factory.Faker('job')


class EmployeeTestCase(TestCase):

    def test_employee(self):
        # Generate a fake employee instance
        employee = EmployeeFactory()
        # Test assertions
        self.assertIsNotNone(employee.last_name)
        self.assertIsNotNone(employee.first_name)
        self.assertIsNotNone(employee.job)

    def test_another_employee(self):
        # Generate a fake employee with an explicit last_name
        employee = EmployeeFactory(last_name='Nakamura')
        # Test assertions
        self.assertTrue(employee.last_name, 'Nakamura')
        self.assertIsNotNone(employee.first_name)
        self.assertIsNotNone(employee.job)