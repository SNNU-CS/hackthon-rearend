from django.conf.urls import url
from . import views
from .views import ActivityView
urlpatterns = [
    url(r'', ActivityView.as_view()),
]
