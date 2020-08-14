from django.test import TestCase
from .models import Developer, Submission, Votes, tags

# Create your tests here.
class DeveloperTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.fred = Developer(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')
    
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fred, Developer))
