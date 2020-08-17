from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime as dt

from .models import Submission, tags, Votes, AwardsAPI
from .serializers import AwardSerializer
from .forms import AwardsForm, NewSubmissionForm
from .email import send_welcome_email
from .permissions import IsAdminOrReadOnly

# Create your views here.
@login_required(login_url = '/accounts/login')
def welcome(request):
    submissions = Submission.objects.all()
    
    if request.method == 'POST':
        form = AwardsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = AwardNewsRecipient(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            
            HttpResponseRedirect('welcome')
        
    else:
        form = AwardsForm()

    context = {"submissions": submissions, "awardsform": form}
    return render(request, 'welcome.html', context)

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

@login_required(login_url = '/accounts/login')
def new_submission(request):
    current_user = request.user
    if request.method == 'post':
        form = NewSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.developer = current_user
            submission.save()
        return redirect('welcome')

    else:
        form = NewSubmissionForm()
    
    context = {"form": form}
    return render(request, 'new_submission.html', context)

class AwardList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_awards = AwardsAPI.objects.all()
        serializers = AwardSerializer(all_awards, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = AwardSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AwardDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_award(self, pk):
        try:
            return AwardsAPI.objects.get(pk=pk)
        except AwardsAPI.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        award = self.get_award(pk)
        serializers = AwardSerializer(award)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        award = self.get_award(pk)
        serializers = AwardSerializer(award, request.data)
        if serializer.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        award = self.get_award(pk)
        award.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)