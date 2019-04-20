from django.conf.urls import url
from . import views
from .views import ActivityView, ActivityListView, UserActivityView
urlpatterns = [
    url(r'^user/(?P<id>[\w\W]+)/', UserActivityView.as_view()),
    url(r'list/', ActivityListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/', ActivityView.as_view()),
    url(r'', ActivityView.as_view()),
]
