from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Submission(models.Model):
    title = models.CharField(max_length=60)
    description = HTMLField()
    developer = models.ForeignKey(User, blank=True, null=True)
    url_link = models.CharField(max_length=40)
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
    content = models.IntegerField()
    submission = models.ForeignKey(Submission, on_delete= models.DO_NOTHING)
    developer = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.submission.title

class AwardNewsRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

class AwardsAPI(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    developer = models.CharField(max_length=40)
    url_link = models.CharField(max_length=40)
