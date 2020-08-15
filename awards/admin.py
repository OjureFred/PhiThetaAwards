from django.contrib import admin
from .models import Submission, Votes, tags

# Register your models here.
class SubmissionAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Votes)
admin.site.register(tags)
