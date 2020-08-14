from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

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
