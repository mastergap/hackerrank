from unittest import TestCase
from bin import Implementation


class TestImplementation(TestCase):

    def test_check_present_students(self):
        Implementation.check_present_students()
        self.fail()
