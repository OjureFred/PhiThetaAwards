#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url(r'^submission/(\d+)', views.submission, name="submission"),
    url(r'^search/', views.search_results, name='search_results'),
    #path('submission/<int:pk>', views.submission, name="submission"),
    url(r'^new/submission$', views.new_submission, name='new-submission'),
    url(r'^vote/(\d+)', views.new_vote, name='new-vote'),
    url(r'^api/awards/$', views.AwardList.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)