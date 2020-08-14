from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import Developer, Submission, tags, Votes

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def submissions_today(request):
    date = dt.date.today()
    submissions = Submission.todays_submission()
    context = {"date": date, "news": news}
    return render(request, 'all-awards/today_submission.html', context)

def past_days_submission(request, past_date):
    try:
        #Converrts data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(submissions_today)

    submissions = Submission.days_submission(date)
    context = {"date": date, "submissions": submissions}
    return render(request, 'all-awards/past-submissions.html', context)

def search_results(request):

    if 'submission' in request.GET and request.GET["submission"]:
        search_term = request.GET.get("submission")
        searched_submissions = Submission.search_by_title(search_term)
        message = f'{search_term}'

        context = {"message": message, "submissions": searched_submissions}
        return render(request, 'all-awards/search.html', context)

    else:
        message = "You haven't searched for any term"
        context = {"message": message}
        return render(request, 'all-awards/search.html', context)

def submission(request, submission_id):
    try:
        submission = Submission.objects.get(id=submission_id)
    except DoesNotExist:
        raise Http404

    context = {"submission": submission}
    return render(request, "all-awards/award.html", context)
