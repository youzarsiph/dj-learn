""" URLConf for dj-learn """

from django.urls import path
from dj_learn import views


# Create your URLConf here
urlpatterns = [
    path("", views.index, name="index"),
]
