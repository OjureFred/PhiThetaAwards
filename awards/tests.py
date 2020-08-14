from django.test import TestCase
from .models import Developer, Submission, Votes, tags
import datetime as dt

# Create your tests here.
class DeveloperTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.fred = Developer(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')
    
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fred, Developer))
    
    #Test save method
    def test_save_method(self):
        self.fred.save_developer()
        developers = Developer.objects.all()
        self.assertTrue(len(developers) > 0)

class SubmissionTestClass(TestCase):

    def setUp(self):
        #Create developer aand save
        self.fred = Developer(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')
        self.fred.save_developer()

        #Create tag and save
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_submission = Submission(title='Test submission', description='Test description', developer=self.fred,
        url_link='test link', date_judged=dt.date(2020, 7, 15), submission_date=dt.date(2020, 6, 20))
        self.new_submission.save()

        self.new_submission.tags.add(self.new_tag)
    
    def tearDown(self):
        Developer.objects.all().delete()
        tags.objects.all().delete()





