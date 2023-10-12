from django.urls import path
from .views import *

urlpatterns = [
    path("", menu),
    path("<slug:main_slug>/", main_category, name="main"),
    path("<slug:main_slug>/<slug:sub_slug>/", sub_category, name="sub")
]
