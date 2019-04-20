from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import UserView

urlpatterns = [path('', UserView.as_view())]
