from django.contrib import admin
from .models import Developer, Submission, Votes, tags

# Register your models here.
class SubmissionAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    
admin.site.register(Developer)
admin.site.register(Submission)
admin.site.register(Votes)
admin.site.register(tags)
