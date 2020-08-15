from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Submission(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    developer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    url_link = models.CharField(max_length=40)
    date_judged = models.DateTimeField()
    tags = models.ManyToManyField(tags)
    submission_date = models.DateTimeField(auto_now_add=True)
    submission_image = models.ImageField(upload_to='submissions/')

    def __str__(self):
        return self.title
    
    @classmethod
    def today_submission(cls):
        today = dt.date.today()
        submissions = cls.objects.filter(submission_date=today)
        return submissions
    
    @classmethod
    def days_submission(cls, date):
        submissions = cls.objects.filter(submission_date=date)
        return submissions

class Votes(models.Model):
    design = models.IntegerField()
    usability = models.IntegerField()
    creativity = models.IntegerField()
    content = models.IntegerField()
    mobile = models.IntegerField()
    submission = models.ForeignKey(Submission, on_delete= models.DO_NOTHING)
    developer = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.submission.title

class AwardNewsRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
